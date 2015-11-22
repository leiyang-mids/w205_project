# setup variables


# define headers
header_segment = [['id','name','climb_category','climb_category_desc',
                  'start_latlng','end_latlng','elev_difference','avg_grade','distance',
                  'activity_type','maximum_grade','elevation_high','elevation_low',
                  'city','state','effort_count','athlete_count','hazardous','star_count']]
file_segment = 'segments.csv'

header_leaderboard = [['seg_id','effort_id','athlete_id','athlete_name','athlete_gender','average_hr',
                       'average_watts','distance','elapsed_time','moving_time','activity_id','rank']]
file_leaderboard = 'leaderboard.csv'

header_stream = [['seg_id','distance','altitude','latlng']]
file_streams = 'segment_streams.csv'

header_activity = [['activity_id','name','distance','moving_time','elapsed_time','total_elevation_gain',
					'type','start_date','athlete_count','trainer','commute','manual','average_speed',
					'average_watts','average_heartrate','max_heartrate','average_cadence',
					'calories','description','kilojoules']]
file_activity = 'activities.csv'

header_act_stream = [['seg_id','distance','altitude']]
file_act_stream = 'activity_streams.csv'

# initialize API client
#global client
client = Client(access_token='9af471894fee3401d0fdfa605494a2b6106d1604')
#client = Client(access_token='763cf38950a862fa1dd831d505bd6768f8d0f612')
#athlete = client.get_athlete()
