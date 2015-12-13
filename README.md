# Path Finder - A Segment Search Tool Based on Strava Data
## MIDS W205 Final Project, Fall 2015
## Lei Yang | Nilesh Bhoyar | Tuhin Mahmud

[Presentation](https://docs.google.com/presentation/d/1pim14yNgvikb0B_u9qBCHCCKgfz6F1oQElEXCFS8BZs/edit?usp=sharing) | [Report](https://docs.google.com/document/d/1Re0OAcl693crMTo4GkVPOpoh8rliut2znPDM0IlNpRE/edit?usp=sharing)

### Deployment Guide
#### System Requirement
1. Port 8330 is open for communication
2. Python, Postgres, Hive, and hiveserver2 are installed and properly configured
3. The following Python libraries are installed:
<pre><code>
 # pip install pyhs2
 # pip install pyhs2
 # pip install psycopg2
 # pip install stravalib
</code></pre>

#### Data Ingestion (as W205)
1. For demo, we have retrieved history data via *Strava API* and stored the csv files on S3.
2. under **/data_transfer_ingestion**, load data lake:
<pre><code># ./load_data_lake.sh</code></pre>
3. An example log file is uploaded in the folder to illustrate a successful ingestion process.

#### Data Transfer
1. under **/data_transfer_ingestion**, create Hive external table for initial exploration:       
<pre><code># hive -f hive_base_ddl.sql</code></pre>
2. under **/data_transfer_ingestion**, create managed tables for segment meta data, leaderboard data, segment geo location data, and activity data:
<pre><code>
 # hive -f hive_segment_ddl.sql
 # hive -f hive_leaderboard_ddl.sql
 # hive -f hive_stream_ddl.sql
 # hive -f hive_activity_ddl.sql
</code></pre>

#### Data Processing
1. under **/data_processing**, create database and tables in Postgres for popular segment:
<pre><code># python postgres_setup.py</code></pre>
2. under **/data_processing**, extract 30 most popular segment for each category in every state, and store the stream and meta data in Postgres:
<pre><code># python job.py</code></pre>


#### Data Serving
1. under home of root, create a **cgi-bin** directory:
<pre><code>
 # cd ~
 # mkdir cgi-bin
</code></pre>
2. under **/data_serving**, copy **HQL_SELECT.py** and **SQL_SELECT.py** to **~/cgi-bin** directory and make them executable:
<pre><code>
 # cp *_SELECT.py ~/cgi-bin/
 # cd ~/cgi-bin
 # chmod +x *_SELECT.py      
</code></pre>
3. under home of root, start hiveserver2:
<pre><code>
 # cd ~
 # hive --service hiveserver2
</code></pre>
4. in another bash window, under home of root, start Python CGI service:
<pre><code>
 # cd ~
 # python -m CGIHTTPServer 8330
</code></pre>
5. insert your AWS IP into line: <code>var host = {host ip}</code> of **main.html**;
6. query server is ready to accept request, and note:
  - hiveserver2 can only handle one query at time, sending a new one before the previous complete will cause issue
  - javascript runs asynchronously, thus please be cautious when sending AJAX query and make sure multiple queries (if necessary) are sent sequentially.

#### Data Visualization
1. A simple html page (**main.html**) is made to navigate results, user can:
  - filter segment based on state and category
  - visualize history segment with data from Hive, or popular segment with data from Postgres
2. **d3.js** is used for Voronoi line chart
3. **jquery.dataTables.min.js** is used for displaying data in grid
4. A heatmap is also made to visualize geo-info of the segment
