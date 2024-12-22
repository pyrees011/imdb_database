## SQL Queries and Explanations

### 1. Getting All the Series in the Database
```sql
SELECT 
    tb.primary_title, 
    tb.start_year, 
    tb.runtime_minutes
FROM
    PUBLIC.title_basic tb
WHERE tb.title_type = 'tvSeries';
```
**Explanation:**
- Fetches all TV series titles along with their start year and runtime.
- Filters the data specifically for series, enabling focused analysis.

### 2. Getting Season Count of the Series
```sql
SELECT 
    tb.primary_title, 
    MAX(ts.season_number) AS seasons
FROM
    PUBLIC.title_basic tb
INNER JOIN PUBLIC.title_episode ts ON tb.tconst = ts.parent_tconst
GROUP BY tb.primary_title
ORDER BY seasons DESC;
```
**Explanation:**
- Retrieves the total number of seasons for each series.
- Uses `MAX` to calculate the highest season number available.

### 3. How Many Years the Series Has Been Running
```sql
SELECT 
    tb.primary_title, 
    COALESCE(MAX(tb.end_year), EXTRACT(YEAR FROM CURRENT_DATE)) - COALESCE(MIN(tb.start_year), EXTRACT(YEAR FROM CURRENT_DATE)) AS years_running
FROM 
    public.title_basic tb
INNER JOIN public.title_episode ts ON tb.tconst = ts.parent_tconst
GROUP BY tb.primary_title
ORDER BY years_running DESC;
```
**Explanation:**
- Calculates the number of years each series has been running.
- Handles ongoing series by using the current year when `end_year` is null.

### 4. Getting the Main Cast of the Series (Particular Series)
```sql
SELECT 
    tb.primary_title, 
    nb.primary_name AS cast,
    tp.category AS role
FROM
    PUBLIC.title_principals tp
LEFT JOIN public.title_basic tb ON tp.tconst = tb.tconst
INNER JOIN public.name_basic nb ON tp.nconst = nb.nconst
WHERE tb.tconst = 'tt0000001'
ORDER BY tb.primary_title;
```
**Explanation:**
- Fetches the main cast for a specific TV series.
- Provides detailed information about the cast's roles.

### 5. Getting the Season-by-Season Breakdown of a Series
```sql
SELECT 
    tb.primary_title, 
    ts.season_number, 
    COUNT(ts.tconst) AS episodes
FROM
    PUBLIC.title_basic tb
INNER JOIN PUBLIC.title_episode ts ON tb.tconst = ts.parent_tconst
WHERE tb.tconst = 'tt0000001'
GROUP BY tb.primary_title, ts.season_number
ORDER BY ts.season_number;
```
**Explanation:**
- Provides a breakdown of the number of episodes per season for a specific series.
- Useful for understanding the content structure of a series.