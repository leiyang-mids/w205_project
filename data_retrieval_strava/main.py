# get libraries
from stravalib import Client
import warnings
import os.path
import sys
warnings.filterwarnings('ignore')

# get source files
from getLeaderBoardActivities import *
from getLeaderBoardAttempts import *
from getSegmentsInSquare import *
from getSegmentStreams import *
#from getActivityStreams import *
from saveArrayToCSV import *
# setup
execfile("setup.py")

# open a file
if (not os.path.isfile(file_segment)):
	saveArrayToCSV(header_segment, file_segment)
if (not os.path.isfile(file_leaderboard)):
	saveArrayToCSV(header_leaderboard, file_leaderboard)
if (not os.path.isfile(file_streams)):
	saveArrayToCSV(header_stream, file_streams)
if (not os.path.isfile(file_activity)):
	saveArrayToCSV(header_activity, file_activity)
#if (not os.path.isfile(file_act_stream)):
#	saveArrayToCSV(header_act_stream, file_act_stream)

# retrieve info
# 1. specify geo range for a city/place
#lat1, lon1, lat2, lon2 = 30.091243, -97.988489, 30.617396, -97.433679  # Austin, TX
#lat1, lon1, lat2, lon2 = 38.790184, -107.567708, 40.719907, -104.376179  # Denver, CO
#lat1, lon1, lat2, lon2 = 40.572189, -74.877846, 41.894049, -71.993935  # NYC metro, NY
#lat1, lon1, lat2, lon2 = 36.870949, -122.808137, 39.316351, -118.886018  # Bay Area, CA
lat1, lon1, lat2, lon2 = 45.125420, -124.497473, 50.568858, -118.825430  # around Seattle, WA 

# 2. divide the range into a grid for scan
n = 40
del_lat, del_lon = (lat2-lat1)/n, (lon2-lon1)/n
grids = []
for i in range(n):
	for j in range(n):
		grids.append([lat1+i*del_lat, lon1+j*del_lon, lat1+(i+1)*del_lat, lon1+(j+1)*del_lon])

# 3. retrieve and save info in each grid
for i in range(n*n):
	try:
		print 'retrieving %s/%s: %s' %(i+1, n*n, str(grids[i]))
		segments, o_seg = getSegmentsInSquare(client, grids[i])
		# continue if no segments
		if (len(segments) == 0):
			print 'no segment in the grid!'
			continue
		else:
			print len(segments), 'segments returned.'
		leaderboard, attempts = getLeaderBoardAttempts(o_seg)
		seg_streams = getSegmentStreams(client, segments)
		activities = getLeaderBoardActivities(attempts)
		#act_streams = getActivityStreams(client, attempts) # doesn't work can't authorize, must be activity owner

		saveArrayToCSV(segments, file_segment)
		saveArrayToCSV(leaderboard, file_leaderboard)
		saveArrayToCSV(seg_streams, file_streams)
		saveArrayToCSV(activities, file_activity)
		#saveArrayToCSV(act_streams, file_act_stream)
	except:
		print 'error in retrieving, skip 1 grid, ', sys.exc_info()[0]

print '\nRetrieving completed!'
