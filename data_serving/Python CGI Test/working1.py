#!/usr/bin/python

import json
import cgi
import pyhs2

# get input data
data = cgi.FieldStorage()
temp = data['hql'].value

response = []
# do whatever you want here
with pyhs2.connect(host='localhost',
                   port=10000,
                   authMechanism="PLAIN",
                   user='root',
                   #password='test',
                   database='default') as conn:

    with conn.cursor() as cur:
        #Show databases
        #print cur.getDatabases()

        #Execute query
        #SQL = "select count(*) as cnt from crimes"
        SQL = "select * from e_activities limit 15"

        cur.execute(SQL)

        #Return column info from query
        #print cur.getSchema()

        #Fetch table results
        for i in cur.fetch():
            response.append({'f1':i[0], 'f2':i[1]})

# assemble output
#response={'Price':temp,'Cost':data['p2'].value}

# dump output json - don't change any line
print 'Content-type: application/json'
print
print json.JSONEncoder().encode(response)
