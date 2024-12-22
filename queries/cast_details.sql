-- getting all actors with a role
--@block
select 
    tb.primary_title,
    nb.primary_name as cast,
    tp.category as role
from
    PUBLIC.title_principals tp
left join PUBLIC.title_basic tb on tp.tconst = tb.tconst
inner join PUBLIC.name_basic nb on tp.nconst = nb.nconst
where tp.category = 'actor' or tp.category = 'actress'
order by role;



-- getting all the cast of a movie
--@block
select 
    tb.primary_title,
    nb.primary_name as cast,
	tp.category as role
from
    PUBLIC.title_principals tp
left join PUBLIC.title_basic tb on tp.tconst = tb.tconst
inner join PUBLIC.name_basic nb on tp.nconst = nb.nconst
where tb.tconst = 'tt0000001'
order by role;

-- getting all crew sorted by category
--@block
select 
	nb.primary_name,
	tp.category,
	count(tp.tconst) as opportunity
from
	PUBLIC.title_principals tp
inner join PUBLIC.name_basic nb on nb.nconst = tp.nconst
group by nb.primary_name, tp.category
order by tp.category;
