# Path Finder - A cycling data analytic tool using Apache Hive
### MIDS W205 Final Project, Fall 2015
## Lei Yang | Nilesh Bhoyar | Tuhin Mahmud

[Presentation](https://docs.google.com/presentation/d/1pim14yNgvikb0B_u9qBCHCCKgfz6F1oQElEXCFS8BZs/edit?usp=sharing) | [Report](https://docs.google.com/document/d/1FVOKB-6Q32uH4-GNqpf_DmkC7-OXr4Tz5N_NgpyRvPg/edit?usp=sharing)

### Deployment Guide
#### System Requirement
1. port 8330 is open for communication
2. HDFS, Python, Postgres, Hive, and hiveserver2 are installed and properly configured
3. the following Python libraries are installed:
<pre><code>
$ pip install pyhs2
$ pip install psycopg2
$ pip install stravalib
</code></pre>
4. below directories exist on the system:
 - file:///data
 - hdfs:///user/w205
5. as w205, checkout repo:
<pre><code>git clone git@github.com:leiyang-mids/w205_project.git</code></pre>

#### Data Ingestion
1. for demo, we have retrieved history data via *Strava API* and stored the csv files on S3. The realtime data retrieving process is documented in **data_retrieval_strava** directory.
2. as w205, under **/data_transfer_ingestion**, download data from S3 and load the files into HDFS:
<pre><code>$ ./load_data_lake.sh</code></pre>
3. an example log file is uploaded in the folder to illustrate a successful ingestion process.

#### Data Transfer
1. as w205, under **/data_transfer_ingestion**, create Hive external table for initial exploration:       
<pre><code>$ hive -f hive_base_ddl.sql</code></pre>
2. as w205, under **/data_transfer_ingestion**, create managed tables for segment meta data, leaderboard data, segment geo location data, and activity data:
<pre><code>
$ hive -f hive_segment_ddl.sql
$ hive -f hive_leaderboard_ddl.sql
$ hive -f hive_stream_ddl.sql
$ hive -f hive_activity_ddl.sql
</code></pre>

#### Data Processing
1. as w205, under **/data_processing**, create database and tables in Postgres for popular segment:
<pre><code>$ python postgres_setup.py</code></pre>
3. in another bash window, as w205, under home directory **~**, start hiveserver2:
<pre><code>
$ cd ~
$ hive --service hiveserver2
</code></pre>
2. as w205, under **/data_processing**, extract 30 most popular segment for each category in every state, and store the stream and meta data in Postgres (this step take several minutes):
<pre><code>$ python job.py</code></pre>
3. last step would take several minutes, and the bash window would show:
<pre><code>
[w205@ip-172-31-8-168 data_processing]$ python job.py
selecting popular segments...
Populating leaderboard for popular segments...
Populating altitude for popular segments...
Job completed!
</code></pre>

#### Data Serving
1. as w205, in another bash window, under home, create a **cgi-bin** directory:
<pre><code>
$ cd ~
$ mkdir cgi-bin
</code></pre>
2. under **/data_serving**, copy **HQL_SELECT.py** and **SQL_SELECT.py** to **~/cgi-bin** directory and make them executable:
<pre><code>
$ cp *_SELECT.py ~/cgi-bin/
$ cd ~/cgi-bin
$ chmod +x *_SELECT.py      
</code></pre>
4. as w205, under home, start Python CGI service:
<pre><code>
$ cd ~
$ python -m CGIHTTPServer 8330
</code></pre>
5. edit **main.html**, insert your AWS IP into line: <code>var host = {host ip}</code>
6. as w205, under **/data_serving**, copy the website scripts to home:
<code><pre>
$ cp main.html ~/index.html
$ cp *.js ~/
$ cp *.css ~/
</code></pre>
5. AWS host is now ready to accept query request, but note:
  - hiveserver2 can only handle one query at time, sending a new one before the previous complete will cause issue
  - javascript runs asynchronously, thus please be cautious when sending AJAX query and make sure multiple queries (if necessary) are sent sequentially.

#### Data Visualization
1. Open a browser, type in <code>host_ip:8330</code> in the address bar, to navigate results:
  - it takes ~2 minutes initializing the page, to populate the dropdowns. The speed here needs improvement
  - filter segment based on state and category
  - visualize history segment with data from Hive, or popular segment with data from Postgres
  - during the Visualization process, both CGI and hiveserver2 should show query process, and the browser console also has log to indicate the data transfer.
2. **d3.js** is used for Voronoi line chart
3. **jquery.dataTables.min.js** is used for displaying data in grid
4. A heatmap is also made to visualize geo-info of the segment
