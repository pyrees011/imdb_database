'''
This is the schema for the name_basic table. This table contains the following columns:
- nconst: VARCHAR PRIMARY KEY
- primary_name: name of the person
- birth_year: year of birth
- death_year: year of death
'''

from connection.db_connect import db_connect, db_close

conn, cur = db_connect()

cur.execute("""
CREATE TABLE name_basic (
    nconst VARCHAR PRIMARY KEY,
    primary_name VARCHAR NOT NULL,
    birth_year INT,
    death_year INT
);
""")

conn.commit()
print('Table name_basic created successfully')

db_close()