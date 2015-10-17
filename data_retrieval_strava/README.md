Strava data retrieval module

1. main.py - set location square for a city on line 32, for lower-left (1) and upper-right (2) points.
2. 4 CSV files are saved after main execution:
3. activities.csv      - activity summary from the leader board
4. leaderboard.csv     - leader board for various segments
5. segments.csv        - segment info in the area
6. segment_streams.csv - stream data (lotlat, altitude, distance) fro segment
7. python package needs to be installed: pip install stravalib
