-- to display column name in the query
set hive.cli.print.header = true;

-- external table for activities.csv
drop table e_activities;
create external table e_activities (
  activity_id string,
  name string,
  distance string,
  moving_time string,
  elapsed_time string,
  total_elevation_gain string,
  type string,
  start_date string,
  athlete_count string,
  trainer string,
  commute string,
  manual string,
  average_speed string,
  average_watts string,
  average_heartrate string,
  max_heartrate string,
  average_cadence string,
  calories string,
  description string,
  kilojoules string
)
row format delimited
fields terminated by ','
stored as textfile
location '/user/w205/project/activities_csv';

-- external table for leaderboard.csv
drop table e_leaderboard;
create external table e_leaderboard (
  seg_id string,
  effort_id string,
  athlete_id string,
  athlete_name string,
  athlete_gender string,
  average_hr string,
  average_watts string,
  distance string,
  elapsed_time string,
  moving_time string,
  activity_id string,
  rank string
)
row format delimited
fields terminated by ','
stored as textfile
location '/user/w205/project/leaderboard_csv';

-- external table for segments.csv
drop table e_segments;
create external table e_segments (
  id string,
  name string,
  climb_category string,
  climb_category_desc string,
  start_lat string,
  start_lng string,
  end_lat string,
  end_lng string,
  elev_difference string,
  avg_grade string,
  distance string,
  activity_type string,
  maximum_grade string,
  elevation_high string,
  elevation_low string,
  city string,
  state string,
  effort_count string,
  athlete_count string,
  hazardous string,
  star_count string
)
row format delimited
fields terminated by ','
stored as textfile
location '/user/w205/project/segments_csv';

-- external table for wide_segment_streams.csv
drop table e_streams;
create external table e_streams (
  seg_id string,
  distance string,
  altitude string,
  latitude string,
  longitude string
)
row format delimited
fields terminated by ','
stored as textfile
location '/user/w205/project/wide_segment_streams_csv';
