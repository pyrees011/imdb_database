'''
This is the schema for the title_principals table. This table contains the following columns:
- tconst: VARCHAR
- ordering: unique identifier for the principal with respect to the title
- nconst: VARCHAR
- category: category of the principal
- job: job of the principal
- characters: characters played by the principal
'''

from connection.db_connect import db_connect, db_close

conn, cur = db_connect()

cur.execute("""
CREATE TABLE title_principals (
    tconst VARCHAR,
    ordering INT,
    nconst VARCHAR,
    category VARCHAR,
    job VARCHAR,
    characters VARCHAR,
    PRIMARY KEY (tconst, ordering),
    FOREIGN KEY (tconst) REFERENCES title_basic(tconst),
    FOREIGN KEY (nconst) REFERENCES name_basic(nconst)
);
""")

conn.commit()
print('Table title_principals created successfully')

db_close()