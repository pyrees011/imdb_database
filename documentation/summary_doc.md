## SQL Queries and Explanations

### 1. Title, Year, and Runtime of the Movies
```sql
SELECT 
    tb.primary_title, 
    tb.start_year, 
    tb.runtime_minutes 
FROM
    PUBLIC.title_basic tb;
```
**Explanation:**
- Retrieves the basic information of movies, including title, release year, and runtime.
- Useful for creating a general overview of the available titles.

### 2. Getting the Writers and Directors of the Movies
```sql
SELECT 
    tb.primary_title, 
    STRING_AGG(nd.primary_name, ', ') AS directors, 
    STRING_AGG(nw.primary_name, ', ') AS writers 
FROM 
    public.title_basic tb
INNER JOIN public.title_directors td ON tb.tconst = td.tconst
INNER JOIN public.title_writers tw ON tb.tconst = tw.tconst
INNER JOIN public.name_basic nd ON td.nconst = nd.nconst
INNER JOIN public.name_basic nw ON tw.nconst = nw.nconst
GROUP BY tb.primary_title;
```
**Explanation:**
- Fetches movie titles along with their directors and writers.
- Uses `STRING_AGG` to concatenate names for better readability.

### 3. Getting the Main Cast of Five Movies
```sql
SELECT 
    tb.primary_title, 
    nb.primary_name AS cast 
FROM 
    PUBLIC.title_principals tp
LEFT JOIN public.title_basic tb ON tp.tconst = tb.tconst
INNER JOIN public.name_basic nb ON tp.nconst = nb.nconst
WHERE tp.category = 'actor' OR tp.category = 'actress'
LIMIT 5;
```
**Explanation:**
- Retrieves the main cast for five movies.
- Filters the data to include only actors and actresses.
- Provides a quick insight into the prominent members of a title's cast.

### 4. Getting the Ratings and Number of Votes for Movies
```sql
SELECT 
    tb.primary_title, 
    tr.average_rating, 
    tr.num_votes 
FROM PUBLIC.title_ratings tr
LEFT JOIN PUBLIC.title_basic tb ON tr.tconst = tb.tconst;
```
**Explanation:**
- Fetches ratings and vote counts for movies.
- Useful for analyzing the popularity and reception of titles.

### 5. Getting the Basic Info of the Movies
```sql
SELECT 
    tb.primary_title,
    tb.title_type,
    STRING_AGG(gb.genre, ', ') AS genres
FROM
    PUBLIC.title_basic tb
INNER JOIN PUBLIC.title_genre gb ON tb.tconst = gb.tconst
GROUP BY tb.primary_title, tb.title_type
ORDER BY tb.title_type;
```
**Explanation:**
- Combines movie titles with their type and associated genres.
- Uses `STRING_AGG` to display genres as a comma-separated list.
- Helps categorize titles based on their genres and types.

---

## Suggestions for Additional Analyses

1. **Genre Popularity Over Time:**
   - Analyze how the popularity of different genres has evolved over decades.
   - Use the `title_genre` and `title_basic` tables.

2. **Collaborative Networks:**
   - Identify frequently collaborating directors and writers.
   - Leverage `title_directors` and `title_writers` for relationships.

3. **Actor Success Trends:**
   - Evaluate the average ratings of movies for each actor.
   - Combine `title_principals` and `title_ratings` for this analysis.

4. **Episode Ratings:**
   - Compare the average ratings of episodes across different TV series.
   - Utilize the `title_episode` and `title_ratings` tables.