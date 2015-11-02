DROP TABLE IF EXISTS TR_activities;
create table TR_activities
AS select  activity_id,
           name,
           distance,
           moving_time,
           elapsed_time,
           total_elevation_gain,
           type,
           start_date,
           athlete_count,
           trainer,
           commute,
           manual,
           average_speed,
           average_watts,
           average_heartrate,
           max_heartrate,
           average_cadence,
           calories,
           description,
           kilojoules
from  e_activities;


DROP TABLE IF EXISTS TR_leaderboard;
create table TR_leaderboard
AS select  seg_id,
           effort_id,
           athlete_id,
           athlete_name,
           athlete_gender,
           average_hr,
           average_watts,
           distance,
           elapsed_time,
           moving_time,
           activity_id,
           rank
from  e_leaderboard;

DROP TABLE IF EXISTS TR_segment;
create table TR_segment
AS select id as seg_id,
          name,
          climb_category,
          climb_category_desc,
          start_lat,
          start_lng,
          end_lat,
          end_lng,
          elev_difference,
          avg_grade,
          distance,
          activity_type,
          maximum_grade,
          elevation_high,
          elevation_low,
          city,
          state,
          effort_count,
          athlete_count,
          hazardous,
          star_count
from e_segments;


DROP TABLE IF EXISTS TR_streams;
create table TR_streams
AS select s.seg_id,
          s.city,
          s.state,
          d.distance,
          d.altitude,
          d.latitude,
          d.longitude
from e_segments s join e_streams d on s.id = d.seg_id
PARTITIONED BY (s.state string)
