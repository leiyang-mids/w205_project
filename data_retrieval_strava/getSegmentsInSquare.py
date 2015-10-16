# retrieve segments 
def getSegmentsInSquare(squareCoord):
    segs = client.explore_segments(squareCoord)    
    info = []
    for seg in segs:
        detail = seg.segment
        info.append([str(seg.id),
             str(seg.name),
             str(seg.climb_category),
             str(seg.climb_category_desc),
             str(seg.start_latlng),
             str(seg.end_latlng),
             str(seg.elev_difference),
             str(seg.avg_grade),
             str(seg.distance),
             str(detail.activity_type),
             str(detail.maximum_grade),
             str(detail.elevation_high),
             str(detail.elevation_low),
             str(detail.city),
             str(detail.state),
             str(detail.effort_count),
             str(detail.athlete_count),
             str(detail.hazardous),
             str(detail.star_count)])
    
    # get leaderboard info
    leaderboard = []
    for seg in segs:
        for attemp in seg.segment.leaderboard.entries:
            leaderboard.append([str(seg.id),
                  str(attemp.effort_id),
                  str(attemp.athlete_id),
                  str(attemp.athlete_name),
                  str(attemp.athlete_gender),
                  str(attemp.average_hr),
                  str(attemp.average_watts),
                  str(attemp.distance),
                  str(attemp.elapsed_time),
                  str(attemp.moving_time),
                  str(attemp.activity_id),
                  str(attemp.rank)])
                   
    # return results
    return info, leaderboard
