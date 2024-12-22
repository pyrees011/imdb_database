import pandas as pd
from connection.db_connect import db_connect, db_close

# Helper function to clean '\\N' values and cast to integers if applicable
def clean_int(value):
    return int(value) if value != '\\N' else None

# Helper function to process a chunk of data
def process_basics_chunk(chunk, cursor):
    # Prepare data for `title_basic`
    chunk['startYear'] = chunk['startYear'].apply(clean_int)
    chunk['endYear'] = chunk['endYear'].apply(clean_int)
    chunk['runtimeMinutes'] = chunk['runtimeMinutes'].apply(clean_int)
    chunk['genres'] = chunk['genres'].apply(lambda x: x.split(',') if x != '\\N' else [])

    basic_records = chunk[['tconst', 'titleType', 'primaryTitle', 'originalTitle', 'isAdult', 
                           'startYear', 'endYear', 'runtimeMinutes']].values.tolist()

    # Insert into `title_basic`
    cursor.executemany("""
        INSERT INTO title_basic (tconst, title_type, primary_title, original_title, is_adult, start_year, end_year, runtime_minutes)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (tconst) DO UPDATE 
        SET title_type = EXCLUDED.title_type,
            primary_title = EXCLUDED.primary_title,
            original_title = EXCLUDED.original_title,
            is_adult = EXCLUDED.is_adult,
            start_year = EXCLUDED.start_year,
            end_year = EXCLUDED.end_year,
            runtime_minutes = EXCLUDED.runtime_minutes;
    """, basic_records)

    # Prepare data for `title_genre`
    genre_records = []
    for _, row in chunk.iterrows():
        tconst = row['tconst']
        genres = row['genres']
        genre_records.extend([(tconst, genre) for genre in genres])

    # Insert into `title_genre`
    if genre_records:
        cursor.executemany("""
            INSERT INTO title_genre (tconst, genre)
            VALUES (%s, %s)
            ON CONFLICT DO NOTHING;
        """, genre_records)

conn, cur = db_connect()

try:
    file_path = 'title.basics.tsv'
    chunk_size = 100000

    for chunk in pd.read_csv(file_path, sep='\t', chunksize=chunk_size):
        print("Processing a new chunk...")
        process_basics_chunk(chunk, cur)

    conn.commit()
    print("Data inserted successfully.")
except Exception as e:
    conn.rollback()
    print(f"Error: {e}")
finally:
    db_close()
