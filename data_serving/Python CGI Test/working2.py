#!/usr/bin/python

import json
import cgi
import pyhs2

# get input data
data = cgi.FieldStorage()
temp = data['p1'].value

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
        #SQL = "select * from e_activities limit 15"
	SQL = "select * from crimes limit 100"

        cur.execute(SQL)

        #Return column info from query
        #print cur.getSchema()

        #Fetch table results
        for i in cur.fetch():
            response.append({'f1':i[6], 'f2':i[5]})

# assemble output
#response={'Price':temp,'Cost':data['p2'].value}                                                                                               
