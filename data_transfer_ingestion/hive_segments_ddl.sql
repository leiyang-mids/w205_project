-- segment table

drop table m_segment;
create table m_segment as
  select distinct
    id, name,
    trim(city) as city,
    case
      when trim(state) in ('CA', 'California', 'Berkeley', 'San Jose', 'Napa') then 'CA'
      when trim(state) in ('NY', 'New York') then 'NY'
      when trim(state) in ('CO', 'Colorado') then 'CO'
      when trim(state) in ('CT', 'Connecticut') then 'CT'
      else state
    end as state,
    cast(climb_category as int) as category,
    cast(split(trim(distance), ' ')[0] as double) as distance,
    cast(effort_count as int) as effort_count
  from e_segments
  where
    --category in (0,1,2,3,4,5) and
    distance > 0 and
    length(state) == 2
  ;
