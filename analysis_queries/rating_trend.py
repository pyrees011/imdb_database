import pandas as pd
import matplotlib.pyplot as plt
from connection.db_connect import db_connect, db_close

# Database connection
conn, cur = db_connect() 

# Query
cur.execute("""
SELECT 
    (start_year / 10) * 10 AS decade,
    AVG(average_rating) AS avg_rating
FROM title_basic
JOIN title_ratings USING (tconst)
WHERE start_year IS NOT NULL
GROUP BY decade
ORDER BY decade;
""")

# Fetch data
data = cur.fetchall()

# Close connection
db_close()

# Dataframe
df = pd.DataFrame(data, columns=['decade', 'avg_rating'])

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df['decade'], df['avg_rating'], marker='o')
plt.title('Average Ratings by Decade')
plt.xlabel('Decade')
plt.ylabel('Average Rating')
plt.grid(True)
plt.show()
