select count(*) as cnt, state from e_segments group by state order by cnt desc;

select count(*) as cnt, climb_category from e_segments group by climb_category order by cnt desc;

select count(*) as cnt, avg_grade from e_segments group by avg_grade order by cnt desc;

select distinct distance from e_segments limit 100;
