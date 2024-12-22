-- getting episode specific details of a series
--@block
select 
	tb.primary_title,
	tb.is_adult,
	tb.start_year,
	tb.runtime_minutes
from PUBLIC.title_episode te
left join PUBLIC.title_basic tb on te.tconst = tb.tconst
where te.parent_tconst = 'tt0000001';

-- getting individual rating of an episode for a series
--@block
select 
    tb.primary_title,
    tr.average_rating,
    tr.num_votes
from 
    PUBLIC.title_episode te
left join PUBLIC.title_basic tb on te.tconst = tb.tconst
left join PUBLIC.title_ratings tr on te.tconst = tr.tconst
where te.parent_tconst = 'tt0000001';
