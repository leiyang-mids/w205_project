# Data Transformation and Ingestion

1. convert_stream.py - convert stream data to wide mode
2. load_data_lake.sh - download csv files from S3, call script above, and load files into HDFS
3. hive_base_ddl.sql - create external table in Hive for initial exploration
4. hive_segment_ddl.sql - create managed table in Hive, perform data cleaning on the critical columns (nuclear approach)
5. hive_stream_ddl.sql - create managed table in Hive for stream data, get rid of invalid entries by joining seg_id with m_segment table.
6. hive_leaderboard_ddl.sql - create managed table in Hive for leaderboard info, get rid of invalid entries by joining seg_id with m_segment table.
