import csv
import numpy as np
import os.path

print 'converting stream data to wide format ...'
source = open('segment_streams.csv', 'r')
header = source.readline()
destFileName = 'wide_segment_streams.csv'
if (not os.path.isfile(destFileName)):
    np.savetxt(destFileName, [['seg_id','distance','altitude','latitude','longitude']], delimiter=',', fmt='%s')

destination = file(destFileName, 'a')
for line in source:
    cells = line.split(',')
    distance = np.array(cells[1][1:-1].split('|'))
    altitude = np.array(cells[2][1:-1].split('|'))
    if (len(distance)!=len(altitude)):
        print 'dimension mismatch between distance and altitude, skipping segment ' + cells[0]
        continue
    latlng = np.transpose([ll.split('|') for ll in cells[3][2:-3].split(']|[')])
    if (len(np.shape(latlng))<2 or len(distance)!=np.shape(latlng)[1]):
        print 'dimension mismatch between distance and coordinates, skipping segment ' + cells[0]
        continue
    seg_id = np.repeat(cells[0], len(distance))
    segment = np.transpose(np.vstack((seg_id, distance, altitude, latlng)))
    np.savetxt(destination, segment, delimiter=',', fmt='%s')

source.close()
destination.close()
print 'conversion completed!'
