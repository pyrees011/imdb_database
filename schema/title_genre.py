'''
this is the schema for the title_genre table. This table contains the following columns:
- tconst: VARCHAR
- genre: genre of the title
'''

from connection.db_connect import db_connect, db_close

conn, cur = db_connect()

cur.execute("""
CREATE TABLE title_genre (
    tconst VARCHAR,
    genre TEXT,
    PRIMARY KEY (tconst, genre),
    FOREIGN KEY (tconst) REFERENCES title_basic(tconst)
);
""")

conn.commit()
print('Table title_genre created successfully')

db_close()