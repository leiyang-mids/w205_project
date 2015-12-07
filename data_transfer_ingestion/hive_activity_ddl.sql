-- activity tab1Label

drop table m_activity;
create table m_activity as
  select
    l.activity_id as activity_id,
    cast(split(trim(a.distance), ' ')[0] as double) as distance,
    cast(trim(a.athlete_count) as int) as athlete_count,
    cast(split(trim(a.total_elevation_gain), ' ')[0] as double) as total_elevation_gain,
    cast(split(trim(a.average_speed), ' ')[0] as double) as average_speed,
    cast(trim(a.average_watts) as double) as average_watts,
    cast(trim(a.average_heartrate) as double) as average_heartrate,
    cast(trim(a.max_heartrate) as double) as max_heartrate,
    cast(trim(a.average_cadence) as double) as average_cadence,
    cast(trim(a.calories) as double) as calories,
    cast(trim(a.kilojoules) as double) as kilojoules,
    a.name,
    a.start_date,
    a.description,
    a.type,
    a.moving_time,
    a.elapsed_time
  from e_activities a
  inner join m_leaderboard l on a.activity_id = l.activity_id;
