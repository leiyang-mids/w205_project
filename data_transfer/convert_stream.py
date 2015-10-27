import csv
import numpy as np
import os.path

source = open('C:\Users\leyang\Downloads\StravaSample\streams.csv', 'r')
header = source.readline()
destFileName = 'test.csv'
if (not os.path.isfile(destFileName)):
    np.savetxt(destFileName, [['seg_id','distance','altitude','latitude','longitude']], delimiter=',', fmt='%s')
    
destination = file(destFileName, 'a')
for line in source:
    cells = line.split(',')
    distance = np.array(cells[1][1:-1].split('|'))
    length = len(distance)
    seg_id = np.repeat(cells[0], length)
    altitude = np.array(cells[2][1:-1].split('|'))
    latlng =[ll.split('|') for ll in cells[3][2:-3].split(']|[')]
    segment = np.transpose(np.vstack((seg_id, distance, altitude, np.transpose(latlng))))
    np.savetxt(destination, segment, delimiter=',', fmt='%s')
    
source.close()
destination.close()
print 'done'
