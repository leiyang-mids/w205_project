echo "# creating /user/w205/weather folder in HDFS ..."

hdfs dfs -rm -r /user/w205/weather

hdfs dfs -mkdir /user/w205/weather


echo "# loading the raw data files into HDFS under /user/w205/weather ..."
hdfs dfs -put /tmp/weather.csv /user/w205/weather/weather.csv

echo "# data loading successfully completed!"