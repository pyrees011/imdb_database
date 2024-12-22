'''
this is the schema for the title_directors table. This table contains the following columns:
- tconst: VARCHAR
- ordering: unique identifier for the director with respect to the title
- nconst: VARCHAR
'''

from connection.db_connect import db_connect, db_close

conn, cur = db_connect()

cur.execute("""
CREATE TABLE title_directors (
    tconst VARCHAR,
    ordering INT,
    nconst VARCHAR,
    PRIMARY KEY (tconst, ordering),
    FOREIGN KEY (tconst) REFERENCES title_basic(tconst),
    FOREIGN KEY (nconst) REFERENCES name_basic(nconst)
);
""")

conn.commit()
print('Table title_directors created successfully')

db_close()
