# MIDS W205 Project

### Data Ingestion (as w205 user)
1. Strava data is extracted via Strava API and stored as csv on S3.
2. To load the files, navigate to data_transfer_ingestion folder, and execute shell script: load_data_lake.sh
3. To create Hive external table for initial exploration, execute SQL script: hive -f hive_base_ddl.sql
4. An example log file is uploaded in the folder to illustrate a successful ingestion process.

File description:
1. main.py - set location square for a city on line 32, for lower-left (1) and upper-right (2) points.
2. 4 CSV files are saved after main execution:
3. activities.csv      - activity summary from the leader board
4. leaderboard.csv     - leader board for various segments
5. segments.csv        - segment info in the area
6. segment_streams.csv - stream data (lotlat, altitude, distance) fro segment
7. python package needs to be installed: pip install stravalib

### Data Transfer
1. Execute hive -f hive_base_ddl.sql to create external tables in Hive for initial exploration.
2. Execute hive -f hive_segment_ddl.sql to create managed table for segment meta data.
3. Execute hive -f hive_leaderboard_ddl.sql to create managed table for segment leaderboard data.
4. Execute hive -f hive_stream_ddl.sql to create managed table for segment geo location data.
5. Execute hive -f hive_activity_ddl.sql to create managed table for activity data of segment.

File description:
1. convert_stream.py - convert stream data to wide mode
2. load_data_lake.sh - download csv files from S3, call script above, and load files into HDFS
3. hive_base_ddl.sql - create external table in Hive for initial exploration
4. hive_segment_ddl.sql - create managed table in Hive, perform data cleaning on the critical columns (nuclear approach)
5. hive_stream_ddl.sql - create managed table in Hive for stream data, get rid of invalid entries by joining seg_id with m_segment table.
6. hive_leaderboard_ddl.sql - create managed table in Hive for leaderboard info, get rid of invalid entries by joining seg_id with m_segment table.

### Data Processing
1. postgres_setup.py - create database and tables in Postgres for popular segment.
2. job.py - extract 30 most popular segment for each category in every state, and store the stream and meta data in Postgres.

### Data Serving
1. open port 10000 and 8330 for communication
2. install hiveserver2, and make sure Hive is running properly
3. install pyhs2 library: pip install pyhs2
4. create a directory cgi-bin under the home of root: mkdir cgi-bin
5. copy HQL_SELECT.py and SQL_SELECT.py to ~/cgi-bin folder (cp *QL_*.py ~/cgi-bin/), and make it executable: chmod +x *QL_*.py
6. as root, start hiveserver2: hive --service hiveserver2
7. as root, under the home directory (~), start Python CGI service: python -m CGIHTTPServer 8330
8. insert your AWS IP into line: var host = '<the AWS host ip>' of main.html;
9. query server is ready to accept request, and note:
  - hiveserver2 can only handle one query at time, sending a new one before the previous complete will cause issue
  - javascript runs asynchronously, thus please be cautious when sending AJAX query and make sure multiple queries (if necessary) are sent sequentially.

Additional Notes:
1. logon to Postgres, as w205: psql –U postgres
2. connect to Postgres DB: \c '[database_name]'

### Data Visualization
1. A simple html page is made to navigate results, user can:
  - filter segment based on state and category
  - visualize history segment with data from Hive, or popular segment with data from Postgres
2. d3.js is used for Voronoi line chart
3. jquery.dataTables.min.js is used for displaying data in grid
4. A heatmap is also made to visualize geo-info of the segment
