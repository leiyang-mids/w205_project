# segments - list of stravalib.model.SegmentExplorerResult
# info     - string array for file saving
# attempts - list of stravalib.model.SegmentLeaderboardEntry

def getLeaderBoardAttempts(segments):
	# get leaderboard info
    attempts, info = [], []
    for seg in segments:
        for attempt in seg.segment.leaderboard.entries:
            attempts.append(attempt)
            info.append([str(seg.id),
                 str(attempt.effort_id),
                 str(attempt.athlete_id),
                 str(attempt.athlete_name),
                 str(attempt.athlete_gender),
                 str(attempt.average_hr),
                 str(attempt.average_watts),
                 str(attempt.distance),
                 str(attempt.elapsed_time),
                 str(attempt.moving_time),
                 str(attempt.activity_id),
                 str(attempt.rank)])

	return info, attempts
