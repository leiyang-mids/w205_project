# attempts - list of stravalib.model.SegmentLeaderboardEntry
# info     - string array for file saving

# get the associated activity from the leaderboard attempt
def getLeaderBoardActivities(attempts):
	info = []
	for attempt in attempts:
		try:
			act = attempt.activity
			info.append([
				str(attempt.activity_id),
				str(act.name),
				str(act.distance),
				str(act.moving_time),
				str(act.elapsed_time),
				str(act.total_elevation_gain),
				str(act.type),
				str(act.start_date),
				str(act.athlete_count),
				str(act.trainer),
				str(act.commute),
				str(act.manual),
				str(act.average_speed),
				str(act.average_watts),
				str(act.average_heartrate),
				str(act.max_heartrate),
				str(act.average_cadence),
				str(act.calories),
				str(act.description),
				#str(act.zones),
				str(act.kilojoules)])
		except:
			print 'parsing error in getLeaderBoardActivities - skip 1 activity'

	return info
