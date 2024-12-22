-- getting movie details

--@block
select 
    tb.primary_title, 
    ta.title, ta.region, 
    ta.language 
from 
    PUBLIC.title_akas ta
inner join PUBLIC.title_basic tb on tb.tconst = ta.tconst 
where tb.tconst = 'tt0000001';

-- getting prodduction details of a movie
--@block
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

-- techinal details of a movie
--@block
select 
    tb.primary_title,
	tb.title_type,
    STRING_AGG(gb.genre, ', ') as genres
from
    PUBLIC.title_basic tb
inner join PUBLIC.title_genre gb on tb.tconst = gb.tconst
where tb.tconst = 'tt0000001'
group by tb.primary_title, tb.title_type
order by tb.title_type;
