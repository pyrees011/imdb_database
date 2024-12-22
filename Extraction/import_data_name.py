import pandas as pd
from connection.db_connect import db_connect, db_close

def clean_column(series):
    """Clean column values by replacing '\\N' with None and ensuring compatibility."""
    return series.replace('\\N', None).where(pd.notnull(series), None)

def process_chunk(chunk, cursor):
    """Process and insert a chunk of data into the database."""
    # Prepare the main table data
    name_basic_data = chunk[['nconst', 'primaryName', 'birthYear', 'deathYear']].copy()
    name_basic_data['birthYear'] = clean_column(name_basic_data['birthYear']).astype('Int64')
    name_basic_data['deathYear'] = clean_column(name_basic_data['deathYear']).astype('Int64')

    # Prepare the professions data
    name_professions_data = (
        chunk[['nconst', 'primaryProfession']]
        .copy()
        .query("primaryProfession != '\\N'")
        .assign(professions=lambda df: df['primaryProfession'].str.split(','))
        .explode('professions')
        .reset_index(drop=True)
    )
    name_professions_data['ordering'] = name_professions_data.groupby('nconst').cumcount() + 1

    # Prepare the known titles data
    name_known_titles_data = (
        chunk[['nconst', 'knownForTitles']]
        .copy()
        .query("knownForTitles != '\\N'")
        .assign(titles=lambda df: df['knownForTitles'].str.split(','))
        .explode('titles')
        .reset_index(drop=True)
    )
    name_known_titles_data['ordering'] = name_known_titles_data.groupby('nconst').cumcount() + 1

    # Insert into name_basic
    cursor.executemany("""
        INSERT INTO name_basic (nconst, primary_name, birth_year, death_year)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (nconst) DO NOTHING;
    """, name_basic_data.values.tolist())

    # Insert into name_professions
    if not name_professions_data.empty:
        cursor.executemany("""
            INSERT INTO name_professions (nconst, ordering, profession)
            VALUES (%s, %s, %s)
            ON CONFLICT (nconst, ordering) DO NOTHING;
        """, name_professions_data[['nconst', 'ordering', 'professions']].values.tolist())

    # Insert into name_known_titles
    if not name_known_titles_data.empty:
        cursor.executemany("""
            INSERT INTO name_known_titles (nconst, ordering, known_title)
            VALUES (%s, %s, %s)
            ON CONFLICT (nconst, ordering) DO NOTHING;
        """, name_known_titles_data[['nconst', 'ordering', 'titles']].values.tolist())

def process_file_in_chunks(file_path, chunk_size, cursor):
    """Process a large file in chunks and insert into the database."""
    for chunk in pd.read_csv(file_path, sep='\t', chunksize=chunk_size):
        print("Processing a new chunk...")
        process_chunk(chunk, cursor)

conn, cur = db_connect()

try:
    file_path = 'name.basics.tsv'
    chunk_size = 100000

    # Process file in chunks
    process_file_in_chunks(file_path, chunk_size, cur)

    conn.commit()
    print("Data inserted successfully.")
except Exception as e:
    conn.rollback()
    print(f"Error: {e}")
finally:
    db_close()
