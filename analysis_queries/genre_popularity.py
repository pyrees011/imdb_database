import pandas as pd
import matplotlib.pyplot as plt
from connection.db_connect import db_connect, db_close

# Database connection
conn, cur = db_connect()

# Query
cur.execute("""
    SELECT 
    SUBSTRING(tb.start_year::TEXT, 1, 3) || '0' AS decade, 
    tg.genre, 
    COUNT(*) AS num_titles,
    AVG(tr.average_rating) AS avg_rating
FROM 
    public.title_basic tb
INNER JOIN public.title_ratings tr ON tb.tconst = tr.tconst
INNER JOIN public.title_genre tg ON tg.tconst = tb.tconst
WHERE tb.start_year IS NOT NULL
GROUP BY 
    decade, tg.genre
ORDER BY 
    decade, avg_rating DESC;
""")

# Fetch data
data = cur.fetchall()

# Close connection
db_close()

# Dataframe
df = pd.DataFrame(data, columns=['decade', 'genres', 'num_titles', 'avg_rating'])

# Pivot table for genre comparison
pivot_df = df.pivot(index='decade', columns='genres', values='avg_rating')

# Plot genres over decades
pivot_df.plot(kind='line', figsize=(12, 8), marker='o')
plt.title('Genre Popularity and Ratings Over Time')
plt.xlabel('Decade')
plt.ylabel('Average Rating')
plt.grid(True)
plt.show()
