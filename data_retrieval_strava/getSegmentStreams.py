# segments - string array given by getSegmentsInSquare

# retrieve segment stream
def getSegmentStreams(client, segments):
    ids = []
    streams = []
    for seg in segments:
        sid = int(seg[0])
        if sid in ids:
            continue
        ids.append(sid)
        stm = client.get_segment_streams(sid,['latlng','altitude','grade_smooth','cadence'])
        streams.append([seg[0], str(stm['distance'].data).replace(', ','|'),
                        str(stm['altitude'].data).replace(', ','|'),
                        str(stm['latlng'].data).replace(', ','|')])
    return streams
