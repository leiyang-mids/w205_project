#! /bin/bash

echo "# creating local folder to download and store the data ..."
mkdir /data/w205project
# copy the convert script to project
cp convert_stream.py /data/w205project
cd /data/w205project



echo "# downloading and unzip the data ..."
wget https://s3-us-west-2.amazonaws.com/w205.data/strava_data.zip

wait

unzip strava_data.zip
python convert_stream.py

echo "# getting rid of header ..."
tail -n +2 "activities.csv" > "activities1.csv"
tail -n +2 "leaderboard.csv" > "leaderboard1.csv"
tail -n +2 "segments.csv" > "segments1.csv"
tail -n +2 "wide_segment_streams.csv" > "wide_segment_streams1.csv"

echo "# creating /user/w205/project folder in HDFS ..."
hdfs dfs -rm -r /user/w205/project
hdfs dfs -mkdir /user/w205/project
hdfs dfs -mkdir /user/w205/project/activities_csv
hdfs dfs -mkdir /user/w205/project/leaderboard_csv
hdfs dfs -mkdir /user/w205/project/segments_csv
hdfs dfs -mkdir /user/w205/project/wide_segment_streams_csv

echo "# loading the raw data files into HDFS under /user/w205/project ..."
hdfs dfs -put activities1.csv /user/w205/project/activities_csv/activities.csv
hdfs dfs -put leaderboard1.csv /user/w205/project/leaderboard_csv/leaderboard.csv
hdfs dfs -put segments1.csv /user/w205/project/segments_csv/segments.csv
hdfs dfs -put wide_segment_streams1.csv /user/w205/project/wide_segment_streams_csv/wide_segment_streams.csv

echo "# data loading successfully completed!"

cd ..
rm /data/w205project -r
echo "# remove local folder, done!"
