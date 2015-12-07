-- leaderboard table

drop table m_leaderboard;
create table m_leaderboard as
  select
    s.id as seg_id,
    cast(split(trim(l.distance), ' ')[0] as double) as distance,
    cast(trim(l.rank) as int) as rank,
    cast(trim(l.average_hr) as double) as average_hr,
    cast(trim(l.average_watts) as double) as average_watts,
    effort_id,
    athlete_name,
    athlete_gender,
    activity_id,
    moving_time,
    elapsed_time
  from e_leaderboard l
  inner join m_segment s on l.seg_id = s.id;
