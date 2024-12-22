## SQL Queries and Explanations

### 17. Getting Episode-Specific Details of a Series
```sql
SELECT 
    tb.primary_title,
    tb.is_adult,
    tb.start_year,
    tb.runtime_minutes
FROM PUBLIC.title_episode te
LEFT JOIN PUBLIC.title_basic tb ON te.tconst = tb.tconst
WHERE te.parent_tconst = 'tt0000001';
```
**Explanation:**
- Retrieves detailed information about individual episodes of a specific series.
- Includes metadata such as whether the content is adult, the release year, and runtime.

### 18. Getting Individual Ratings of an Episode for a Series
```sql
SELECT 
    tb.primary_title,
    tr.average_rating,
    tr.num_votes
FROM 
    PUBLIC.title_episode te
LEFT JOIN PUBLIC.title_basic tb ON te.tconst = tb.tconst
LEFT JOIN PUBLIC.title_ratings tr ON te.tconst = tr.tconst
WHERE te.parent_tconst = 'tt0000001';
```
**Explanation:**
- Fetches ratings and vote counts for individual episodes of a series.
- Useful for analyzing the popularity and reception of specific episodes.