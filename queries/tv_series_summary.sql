-- getting all the series in the database
--@block
select 
    tb.primary_title, 
    tb.start_year, 
    tb.runtime_minutes
from
    PUBLIC.title_basic tb
where tb.title_type = 'tvSeries';

-- geting season count of the series
--@block
select 
    tb.primary_title, 
    max(ts.season_number) as seasons
from
    PUBLIC.title_basic tb
inner join PUBLIC.title_episode ts on tb.tconst = ts.parent_tconst
group by tb.primary_title
order by seasons desc;

-- how many years the series has been running
--@block
SELECT 
    tb.primary_title, 
    COALESCE(MAX(tb.end_year), EXTRACT(YEAR FROM CURRENT_DATE)) - COALESCE(MIN(tb.start_year), EXTRACT(YEAR FROM CURRENT_DATE)) AS years_running
FROM 
    public.title_basic tb
INNER JOIN public.title_episode ts ON tb.tconst = ts.parent_tconst
GROUP BY tb.primary_title
ORDER BY years_running DESC;

-- getting the main cast of the series - particualar series
--@block
select 
    tb.primary_title, 
    nb.primary_name as cast,
	tp.category as role
from
    PUBLIC.title_principals tp
left join public.title_basic tb on tp.tconst = tb.tconst
inner join public.name_basic nb on tp.nconst = nb.nconst
where tb.tconst = 'tt0000001'
order by tb.primary_title;

-- getting the season by season breakdown of a series
--@block
select 
    tb.primary_title, 
    ts.season_number, 
    count(ts.tconst) as episodes
from
    PUBLIC.title_basic tb
inner join PUBLIC.title_episode ts on tb.tconst = ts.parent_tconst
where tb.tconst = 'tt0000001'
group by tb.primary_title, ts.season_number
order by ts.season_number;
