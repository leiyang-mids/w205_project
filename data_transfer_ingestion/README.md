# Data Transformation and Ingestion

1. convert_stream.py - convert stream data to wide mode
2. load_data_lake.sh - download csv files from S3, call script above, and load files into HDFS
3. hive_base_ddl.sql - create external table in Hive for initial exploration
