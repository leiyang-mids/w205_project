select count(*) as cnt, state from e_segments group by state order by cnt desc;

select count(*) as cnt, climb_category from e_segments group by climb_category order by cnt desc;

select count(*) as cnt, avg_grade from e_segments group by avg_grade order by cnt desc;

select distinct distance from e_segments limit 100;

select
  seg.name,
  str.distance,
  str.altitude
from
  m_stream str join m_segment seg on str.seg_id = seg.id
where seg.state = 'TX' and seg.category = 1;
