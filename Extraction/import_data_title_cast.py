import pandas as pd
from connection.db_connect import db_connect, db_close

# Helper function to clean '\\N' values
def clean_value(value):
    return value if value != '\\N' else None

# Helper function to process a single chunk
def process_principals_chunk(chunk, cursor):
    records = chunk[['tconst', 'ordering', 'nconst', 'category', 'job', 'characters']].copy()
    records['category'] = records['category'].apply(clean_value)
    records['job'] = records['job'].apply(clean_value)
    records['characters'] = records['characters'].apply(clean_value)

    data = records.values.tolist()
    cursor.executemany("""
        INSERT INTO title_principals (tconst, ordering, nconst, category, job, characters)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (tconst, ordering, nconst) DO NOTHING;
    """, data)

def process_crew_chunk(chunk, cursor):
    for record in chunk.to_dict(orient='records'):
        tconst = record['tconst']
        directors = record['directors'].split(',') if record['directors'] != '\\N' else []
        writers = record['writers'].split(',') if record['writers'] != '\\N' else []

        director_data = [(tconst, idx, director) for idx, director in enumerate(directors)]
        writer_data = [(tconst, idx, writer) for idx, writer in enumerate(writers)]

        if director_data:
            cursor.executemany("""
                INSERT INTO title_directors (tconst, ordering, nconst)
                VALUES (%s, %s, %s)
                ON CONFLICT DO NOTHING;
            """, director_data)

        if writer_data:
            cursor.executemany("""
                INSERT INTO title_writers (tconst, ordering, nconst)
                VALUES (%s, %s, %s)
                ON CONFLICT DO NOTHING;
            """, writer_data)

conn, cur = db_connect()

try:
    # Process `title.principals.tsv` in chunks
    principals_file = 'title.principals.tsv'
    for chunk in pd.read_csv(principals_file, sep='\t', chunksize=100000):
        process_principals_chunk(chunk, cur)

    # Process `title.crew.tsv`
    crew_file = 'title.crew.tsv'
    crew_data = pd.read_csv(crew_file, sep='\t')
    process_crew_chunk(crew_data, cur)

    conn.commit()
    print("Data inserted successfully.")
except Exception as e:
    conn.rollback()
    print(f"Error: {e}")
finally:
    db_close()
