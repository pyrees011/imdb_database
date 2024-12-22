'''
this is the schema for the title_ratings table. This table contains the following columns:
- tconst: VARCHAR PRIMARY KEY
- average_rating: average rating
- num_votes: number of votes
'''

from connection.db_connect import db_connect, db_close

conn, cur = db_connect()

cur.execute("""
CREATE TABLE title_ratings (
    tconst VARCHAR PRIMARY KEY,
    average_rating FLOAT,
    num_votes INT,
    FOREIGN KEY (tconst) REFERENCES title_basic(tconst)
);
""")

conn.commit()
print('Table title_ratings created successfully')

db_close()
