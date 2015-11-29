-- segment table

drop table m_segment;
create table m_segment as
  select
    id, name,
    trim(city) as city,
    case
      when trim(state) in ('CA', 'California', 'Berkeley', 'San Jose', 'Napa', 'Fremont', 'San Francisco', 'Palo Alto', 'Los Gatos', 'Oakland') then 'CA'
      when trim(state) in ('NY', 'New York', 'Yorktown Heights') then 'NY'
      when trim(state) in ('CO', 'Colorado', 'Denver', 'Boulder', 'Aurora') then 'CO'
      when trim(state) in ('CT', 'Connecticut') then 'CT'
      when trim(state) in ('TX', 'Texas', 'San Antonio', 'Austin') then 'TX'
      when trim(state) in ('WA', 'Washington') then 'WA'
      when trim(state) in ('NJ', 'New Jersey', 'Newark') then 'NJ'
      when trim(state) in ('AR', 'Arkansas') then 'AR'
      when trim(state) in ('LA', 'Louisiana') then 'LA'
      when trim(state) in ('OK', 'Oklahoma') then 'OK'
      when trim(state) in ('BC', 'British Columbia', 'Canada"') then 'BC'
      when trim(state) in ('OR', 'Oregon') then 'OR'
      when trim(state) in ('MS', 'Mississippi') then 'MS'
      when trim(state) in ('MO', 'Missouri') then 'MO'
      else trim(state)
    end as state,
    cast(trim(climb_category) as int) as category,
    cast(split(trim(distance), ' ')[0] as double) as distance,
    cast(trim(effort_count) as int) as effort_count
  from e_segments
  where
    --category in (0,1,2,3,4,5) and
    --distance > 0 and
    length(state) == 2
  ;
