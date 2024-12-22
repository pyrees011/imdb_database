'''
this is the schema for the title_episode table. This table contains the following columns:
- tconst: VARCHAR PRIMARY KEY
- parent_tconst: parent title
- season_number: season number
- episode_number: episode number
'''

from connection.db_connect import db_connect, db_close

conn, cur = db_connect()

cur.execute("""
CREATE TABLE title_episode (
    tconst VARCHAR PRIMARY KEY,
    parent_tconst VARCHAR,
    season_number INT,
    episode_number INT,
    FOREIGN KEY (tconst) REFERENCES title_basic(tconst),
    FOREIGN KEY (parent_tconst) REFERENCES title_basic(tconst)
            
);
""")

conn.commit()
print('Table title_episode created successfully')

db_close()
