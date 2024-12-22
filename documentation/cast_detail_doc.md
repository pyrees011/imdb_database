## SQL Queries and Explanations

### 1. Getting All Actors with a Role
```sql
SELECT 
    tb.primary_title,
    nb.primary_name AS cast,
    tp.category AS role
FROM
    PUBLIC.title_principals tp
LEFT JOIN PUBLIC.title_basic tb ON tp.tconst = tb.tconst
INNER JOIN PUBLIC.name_basic nb ON tp.nconst = nb.nconst
WHERE tp.category = 'actor' OR tp.category = 'actress'
ORDER BY role;
```
**Explanation:**
- Retrieves actors and actresses along with their roles for various movies.
- Helps identify specific contributions of cast members.

### 2. Getting All the Cast of a Movie
```sql
SELECT 
    tb.primary_title,
    nb.primary_name AS cast,
    tp.category AS role
FROM
    PUBLIC.title_principals tp
LEFT JOIN PUBLIC.title_basic tb ON tp.tconst = tb.tconst
INNER JOIN PUBLIC.name_basic nb ON tp.nconst = nb.nconst
WHERE tb.tconst = 'tt0000001'
ORDER BY role;
```
**Explanation:**
- Fetches the complete cast and their roles for a specific movie.
- Useful for detailed analysis of the crew composition.

### 3. Getting All Crew Sorted by Category
```sql
SELECT 
    nb.primary_name,
    tp.category,
    COUNT(tp.tconst) AS opportunity
FROM
    PUBLIC.title_principals tp
INNER JOIN PUBLIC.name_basic nb ON nb.nconst = tp.nconst
GROUP BY nb.primary_name, tp.category
ORDER BY tp.category;
```
**Explanation:**
- Retrieves all crew members sorted by their categories (e.g., actor, director).
- Provides insights into the frequency of different roles across titles.
