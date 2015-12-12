# Path Finder - A Segment Search Tool Based on Strava Data
## MIDS W205 Final Project, Fall 2015
## Lei Yang | Nilesh Bhoyar | Tuhin Mahmud

### Project Presentation: [link](https://docs.google.com/presentation/d/1pim14yNgvikb0B_u9qBCHCCKgfz6F1oQElEXCFS8BZs/edit?usp=sharing)

### Deployment Guide and File Description
#### Data Ingestion (as W205)
1. For demo, we have retrieved history data via Strava API and stored the csv files on S3.
2. To load the files, navigate to data_transfer_ingestion folder, and execute shell script: *./load_data_lake.sh*
3. To create Hive external table for initial exploration, execute SQL script: *hive -f hive_base_ddl.sql*
4. An example log file is uploaded in the folder to illustrate a successful ingestion process.

#### Data Transfer
1. run *hive -f hive_base_ddl.sql* to create external tables in Hive for initial exploration.
2. run *hive -f hive_segment_ddl.sql* to create managed table for segment meta data.
3. run *hive -f hive_leaderboard_ddl.sql* to create managed table for segment leaderboard data.
4. run *hive -f hive_stream_ddl.sql* to create managed table for segment geo location data.
5. run *hive -f hive_activity_ddl.sql* to create managed table for activity data of segment.

#### Data Processing
1. run *python postgres_setup.py* to create database and tables in Postgres for popular segment.
2. run *python job.py* to extract 30 most popular segment for each category in every state, and store the stream and meta data in Postgres.

#### Data Serving
1. open port 10000 and 8330 for communication
2. install hiveserver2, and make sure Hive is running properly
3. install pyhs2 library: pip install pyhs2
4. install psycopg2 library: pip install psycopg2
4. create a directory cgi-bin under the home of root: mkdir cgi-bin
5. navigate to data_serving folder, copy HQL_SELECT.py and SQL_SELECT.py to ~/cgi-bin folder (cp \*_SELECT.py ~/cgi-bin/), and make it executable: chmod +x \*.py
6. as root, start hiveserver2: hive --service hiveserver2
7. as root, under the home directory (~), start Python CGI service: python -m CGIHTTPServer 8330
8. insert your AWS IP into line: var host = '<the AWS host ip>' of main.html;
9. query server is ready to accept request, and note:
  - hiveserver2 can only handle one query at time, sending a new one before the previous complete will cause issue
  - javascript runs asynchronously, thus please be cautious when sending AJAX query and make sure multiple queries (if necessary) are sent sequentially.

#### Data Visualization
1. A simple html page is made to navigate results, user can:
  - filter segment based on state and category
  - visualize history segment with data from Hive, or popular segment with data from Postgres
2. d3.js is used for Voronoi line chart
3. jquery.dataTables.min.js is used for displaying data in grid
4. A heatmap is also made to visualize geo-info of the segment
