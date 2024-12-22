'''
this is the schema for the known_for_title table. This table contains the following columns:
- nconst: VARCHAR
- ordering: unique identifier for the known title with respect to the person
- known_title: known for title
'''

from connection.db_connect import db_connect, db_close

conn, cur = db_connect()

cur.execute("""
CREATE TABLE name_known_titles (
    nconst VARCHAR,
    ordering INT,
    known_title VARCHAR,
    PRIMARY KEY (nconst, ordering),
    FOREIGN KEY (nconst) REFERENCES name_basic(nconst)
);
""")

conn.commit()
print('Table name_known_titles created successfully')

db_close()