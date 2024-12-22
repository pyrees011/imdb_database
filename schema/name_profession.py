'''
this is the schema for the name_professions table. This table contains the following columns:
- nconst: VARCHAR
- ordering: unique identifier for the profession with respect to the person
- profession: known for profession

'''

from connection.db_connect import db_connect, db_close

conn, cur = db_connect()

cur.execute("""
CREATE TABLE name_professions (
    nconst VARCHAR,
    ordering INT,
    profession VARCHAR,
    PRIMARY KEY (nconst, ordering),
    FOREIGN KEY (nconst) REFERENCES name_basic(nconst)
);
""")

conn.commit()
print('Table name_professions created successfully')

db_close()
