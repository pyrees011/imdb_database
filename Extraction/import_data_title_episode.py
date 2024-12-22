import pandas as pd
from connection.db_connect import db_connect, db_close

# Helper function to clean '\\N' values and cast to integers if applicable
def clean_int(value):
    return int(value) if value != '\\N' else None

# Helper function to process a chunk of data
def process_episode_chunk(chunk, cursor):
    chunk['seasonNumber'] = chunk['seasonNumber'].apply(clean_int)
    chunk['episodeNumber'] = chunk['episodeNumber'].apply(clean_int)

    records = chunk[['tconst', 'parentTconst', 'seasonNumber', 'episodeNumber']].values.tolist()

    # Batch insert data
    cursor.executemany("""
        INSERT INTO title_episode (tconst, parent_tconst, season_number, episode_number)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (tconst) DO NOTHING;
    """, records)

conn, cur = db_connect()

try:
    file_path = 'title.episode.tsv'
    chunk_size = 100000

    for chunk in pd.read_csv(file_path, sep='\t', chunksize=chunk_size):
        print("Processing a new chunk...")
        process_episode_chunk(chunk, cur)

    conn.commit()
    print("Data inserted successfully.")
except Exception as e:
    conn.rollback()
    print(f"Error: {e}")
finally:
    db_close()
