import pandas as pd
from connection.db_connect import db_connect, db_close
import matplotlib.pyplot as plt

# Database connection
conn, cur = db_connect()

# Query
cur.execute("""
SELECT 
    nb.primary_name AS person, 
    tp.category, 
    COUNT(DISTINCT tr.tconst) AS num_collaborations, 
    AVG(tr.average_rating) AS avg_rating,
    SUM(tr.num_votes) AS total_votes
FROM 
    public.title_principals tp
INNER JOIN 
    public.name_basic nb ON tp.nconst = nb.nconst
INNER JOIN 
    public.title_ratings tr ON tp.tconst = tr.tconst
GROUP BY 
    nb.primary_name, tp.category
ORDER BY 
    num_collaborations DESC, avg_rating DESC;
""")

# Fetch data
data = cur.fetchall()

# Close connection
db_close()

# Dataframe
df = pd.DataFrame(data, columns=['person', 'category', 'num_collaborations', 'avg_rating', 'total_votes'])

# Ensure the data is sorted by num_collaborations and avg_rating
df = df.sort_values(by=['num_collaborations', 'avg_rating'], ascending=[False, False])

# Plot collaborations with average ratings
plt.figure(figsize=(14, 8))

for category in df['category'].unique():
    subset = df[df['category'] == category]
    plt.bar(subset['person'], subset['avg_rating'], label=category)

plt.title('Top Collaborators with High Average Ratings', fontsize=16)
plt.xlabel('Person', fontsize=12)
plt.ylabel('Average Rating', fontsize=12)
plt.legend(title='Category', fontsize=10)
plt.xticks(rotation=45, fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
