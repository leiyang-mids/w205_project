# squareCoord - coordinates of the square for segment search
# segments    - list of stravalib.model.SegmentExplorerResult
# info        - string array for file saving

# retrieve segments
def getSegmentsInSquare(client, squareCoord):
    #global client
    segments = client.explore_segments(squareCoord)
    info = []
    for seg in segments:
        detail = seg.segment
        try:
            info.append([str(seg.id),
                str(seg.name),
                str(seg.climb_category),
                str(seg.climb_category_desc),
                str(seg.start_latlng),
                str(seg.end_latlng),
                str(seg.elev_difference),
                str(seg.avg_grade),
                str(seg.distance),
			    #str(seg.points),
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
        except:
            print 'parsing error in getSegmentsInSquare - skip 1 segment'

    # return results
    return info, segments
