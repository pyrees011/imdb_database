## SQL Queries and Explanations

### 1. Getting the Basic Info of the Movies
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

### 2. Getting Movie Details
```sql
SELECT 
    tb.primary_title, 
    ta.title, ta.region, 
    ta.language 
FROM 
    PUBLIC.title_akas ta
INNER JOIN PUBLIC.title_basic tb ON tb.tconst = ta.tconst 
WHERE tb.tconst = 'tt0000001';
```
**Explanation:**
- Retrieves alternate titles, their regions, and languages for a specific movie.
- Provides insights into how a movie is localized for different audiences.

### 3. Getting Production Details of a Movie
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
WHERE tb.tconst = 'tt0000001'
GROUP BY tb.primary_title;
```
**Explanation:**
- Fetches the list of directors and writers for a specific movie.
- Helps analyze the creative contributors to a title.

### 4. Getting Technical Details of a Movie
```sql
SELECT 
    tb.primary_title,
    tb.title_type,
    STRING_AGG(gb.genre, ', ') AS genres
FROM
    PUBLIC.title_basic tb
INNER JOIN PUBLIC.title_genre gb ON tb.tconst = gb.tconst
WHERE tb.tconst = 'tt0000001'
GROUP BY tb.primary_title, tb.title_type
ORDER BY tb.title_type;
```
**Explanation:**
- Retrieves technical details like title type and genres for a specific movie.
- Useful for understanding the classification and content of the movie.