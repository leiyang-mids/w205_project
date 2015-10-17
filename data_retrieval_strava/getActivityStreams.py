# attempts - list of stravalib.model.SegmentLeaderboardEntry
# info     - string array for file saving

def getActivityStreams(client, attempts):
	info = []
	for att in attempts:
		stream = client.get_activity_streams(att.activity_id, ['altitude','grade_smooth','cadence'])
		info.append([str(att.activity_id),
					 str(stream['distance'].data).replace(', ','|'),
                     str(stream['altitude'].data).replace(', ','|')])

	return info
