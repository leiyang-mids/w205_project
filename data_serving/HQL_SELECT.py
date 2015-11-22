#!/usr/bin/python

import json
import cgi
import pyhs2

# get input data - assuming parameter from jQuery looks like this:
# data: { hql: 'select count(*) from crimes' }
data = cgi.FieldStorage()
hql = data['hql'].value

response = []
# query hive using pyhs2
with pyhs2.connect(host='localhost',
                   port=10000,
                   authMechanism="PLAIN",
                   user='root',
                   database='default') as conn:

    with conn.cursor() as cur:
        # run the query
        cur.execute(hql)
        # fetch table results and assemble response
        for r in cur.fetch():
            response.append({'row': '|'.join(r)})

# dump output json - don't change any line
print 'Content-type: application/json'
print
print json.JSONEncoder().encode(response)
