-- title, year and runtime of the movies
--@block
Select 
    tb.primary_title, 
    tb.start_year, 
    tb.runtime_minutes 
from
    PUBLIC.title_basic tb;

-- getting the writers and directors of the movies
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
GROUP BY tb.primary_title;

-- getting the main cast of the movies of 5 movies
--@block
select 
    tb.primary_title, 
    nb.primary_name as cast 
from 
    PUBLIC.title_principals tp
left join public.title_basic tb on tp.tconst = tb.tconst
inner join public.name_basic nb on tp.nconst = nb.nconst
where tp.category = 'actor' or tp.category = 'actress'
limit 5;

-- geting the rating and num votes of the movies
--@block
select 
    tb.primary_title, 
    tr.average_rating, 
    tr.num_votes 
from PUBLIC.title_ratings tr
left join PUBLIC.title_basic tb on tr.tconst = tb.tconst;

-- getting the basic info of the movies
--@block
select 
    tb.primary_title,
	tb.title_type,
    STRING_AGG(gb.genre, ', ') as genres
from
    PUBLIC.title_basic tb
inner join PUBLIC.title_genre gb on tb.tconst = gb.tconst
group by tb.primary_title, tb.title_type
order by tb.title_type;




