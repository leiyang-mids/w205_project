import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# create strava database
print 'creating strava database in postgres ...'
conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
cur.execute('DROP DATABASE IF EXISTS strava')
conn.commit()
cur.execute("CREATE DATABASE strava")
conn.commit()
cur.close()
conn.close()
print 'database strava is successfully created!'

# connect to strava database and create table & column
print 'creating segment table in strava ...'
conn = psycopg2.connect(database="strava", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS segment')
conn.commit()
cur.execute('''CREATE TABLE segment
       (id TEXT PRIMARY KEY     NOT NULL,
       name TEXT     NOT NULL,
       city TEXT,
       state TEXT    NOT NULL,
       category TEXT,
       distance decimal,
       effort_count INT);''')
conn.commit()
print 'table segment is successfully created!'

# create leaderboard table
cur.execute('DROP TABLE IF EXISTS leaderboard')
conn.commit()
cur.execute('''CREATE TABLE leaderboard
       (id TEXT PRIMARY KEY     NOT NULL,
       rank INT,
       average_hr decimal,
       average_watts decimal,
       effort_id TEXT,
       athlete_name TEXT,
       athlete_gender TEXT,
       moving_time TEXT,
       elapsed_time TEXT);''')
conn.commit()
print 'table leaderboard is successfully created!'

# create stream table
cur.execute('DROP TABLE IF EXISTS stream')
conn.commit()
cur.execute('''CREATE TABLE stream
       (id TEXT NOT NULL,
       distance decimal,
       altitude decimal);''')
conn.commit()
print 'table stream is successfully created!'

# close connection
cur.close()
conn.close()
print 'postgres setup completed, you are good to go!'
