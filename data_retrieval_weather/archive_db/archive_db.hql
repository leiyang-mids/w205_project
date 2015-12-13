-- external table for weather data
drop table e_weather;
create external table e_weather (

city string,

 date string,            
 temp_lo string,          
 temp_hi  string,        
 temp     string,          
 prcp     string,         
 pressure string,       
 wind     string,         
 snow     string,           
 rain     string,          
 sunrise_time string,     
 sunset_time  string,    
 status       string,     
 weather_cd   string,     
 visibility_distance string,
 dewpoint       string,    
 humidity      string    
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
stored as textfile
location '/user/w205/weather/';

---Create Managed table now
drop table m_weather;
create table m_weather as 
select 
date ,
 temp_lo,
 temp_hi ,
 temp,
 prcp,
 pressure ,
 wind    ,
 snow ,
 rain  ,
 sunrise_time ,
 sunset_time,
 status,
 weather_cd ,
 visibility_distance ,
 dewpoint  ,
 humidity    
from e_weather ;