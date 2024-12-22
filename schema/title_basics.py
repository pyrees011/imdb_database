'''
This is the schema for the title_basic table. This table contains the following columns:
- tconst: VARCHAR PRIMARY KEY
- title_type: type of title
- primary_title: title name
- original_title: original title name
- is_adult: int value to determine if the title is adult content. 0 is False, 1 is True
- start_year: year of release
- end_year: year of end
- runtime_minutes: duration of the title in minutes
'''

from connection.db_connect import db_connect, db_close

conn, cur = db_connect()

cur.execute("""
CREATE TABLE title_basic (
    tconst VARCHAR PRIMARY KEY,
    title_type TEXT NOT NULL,
    primary_title TEXT,
    original_title TEXT,
    is_adult INT NOT NULL,
    start_year INT,
    end_year INT,
    runtime_minutes INT NOT NULL
);
""")

conn.commit()
print('Table title_basic created successfully')

db_close()