import pandas as pd
from connection.db_connect import db_connect, db_close

# Helper function to clean '\\N' values
def clean_value(value):
    return value if value != '\\N' else None

conn, cur = db_connect()

# Load the data in chunks to handle large files
chunk_size = 100000
file_path = 'title.akas.tsv'

try:
    for chunk in pd.read_csv(file_path, sep='\t', chunksize=chunk_size):
        print("Processing a new chunk...")

        # Clean and prepare data for batch insertion
        chunk['title'] = chunk['title'].apply(clean_value)
        chunk['region'] = chunk['region'].apply(clean_value)
        chunk['language'] = chunk['language'].apply(clean_value)
        chunk['types'] = chunk['types'].apply(clean_value)
        chunk['attributes'] = chunk['attributes'].apply(clean_value)
        chunk['isOriginalTitle'] = chunk['isOriginalTitle'].astype(int)

        # Convert DataFrame to list of tuples
        records = chunk[['titleId', 'ordering', 'title', 'region', 'language', 'types', 'attributes', 'isOriginalTitle']].values.tolist()

        # Batch insert using executemany
        cur.executemany("""
            INSERT INTO title_akas (tconst, ordering, title, region, language, types, attributes, is_original_title)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (tconst, ordering) DO NOTHING;
        """, records)

    conn.commit()
    print("Data inserted successfully.")
except Exception as e:
    conn.rollback()
    print(f"Error: {e}")
finally:
    db_close()
