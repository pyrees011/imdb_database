import pandas as pd
from connection.db_connect import db_connect, db_close

# Helper function to process a chunk of data
def process_ratings_chunk(chunk, cursor):
    records = chunk[['tconst', 'averageRating', 'numVotes']].values.tolist()

    # Batch insert data
    cursor.executemany("""
        INSERT INTO title_ratings (tconst, average_rating, num_votes)
        VALUES (%s, %s, %s)
        ON CONFLICT (tconst) DO UPDATE 
        SET average_rating = EXCLUDED.average_rating,
            num_votes = EXCLUDED.num_votes;
    """, records)

conn, cur = db_connect()

try:
    file_path = 'title.ratings.tsv'
    chunk_size = 100000

    for chunk in pd.read_csv(file_path, sep='\t', chunksize=chunk_size):
        print("Processing a new chunk...")
        process_ratings_chunk(chunk, cur)

    conn.commit()
    print("Data inserted successfully.")
except Exception as e:
    conn.rollback()
    print(f"Error: {e}")
finally:
    db_close()
