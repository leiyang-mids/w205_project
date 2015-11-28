# MIDS W205 Project

1. Data Ingestion (as w205 user)
 - Strava data is extracted via Strava API and stored as csv on S3.
 - To load the files, navigate to data_transfer_ingestion folder, and execute shell script: load_data_lake.sh
 - To create Hive external table for initial exploration, execute SQL script: hive -f hive_base_ddl.sql
 - An example log file is uploaded in the folder to illustrate a successful ingestion process.
