'''
This is the schema for the title_akas table. This table contains the following columns:
- tconst: VARCHAR
- ordering: unique identifier for the title with respect to the person
- title: title of the movie
- region: region of the movie
- language: language of the movie
- types: type of the movie
- attributes: attributes of the movie
- is_original_title: is the title original
'''

from connection.db_connect import db_connect, db_close

conn, cur = db_connect()

cur.execute("""
CREATE TABLE title_akas (
    tconst VARCHAR,
    ordering INT,
    title VARCHAR,
    region VARCHAR,
    language VARCHAR,
    types VARCHAR,
    attributes VARCHAR,
    is_original_title INT NOT NULL,
    PRIMARY KEY (tconst, ordering),
    FOREIGN KEY (tconst) REFERENCES title_basic(tconst)
);
""")

conn.commit()
print('Table title_akas created successfully')

db_close()