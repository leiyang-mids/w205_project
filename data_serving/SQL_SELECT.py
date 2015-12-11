#!/usr/bin/python

import json
import cgi
import psycopg2

# input data - assuming parameter from jQuery looks like this:
# data: { sql: 'select count(*) from crimes' }
data = cgi.FieldStorage()
sql = data['sql'].value

response = []
# query hive using pyhs2
conn = psycopg2.connect(database="strava", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

# run the query
cur.execute(sql)
# fetch table results and assemble response
for r in cur.fetchall():
    response.append({'row': '|'.join(str(a) for a in r)})

cur.close()
conn.close()

# dump output json - don't change any line
print 'Content-type: application/json'
print
print json.JSONEncoder().encode(response)
