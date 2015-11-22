############################### pyhs2 API ###############################

# connect.cursor()
# connect.close()

# cursor.execute(string hql)
# cursor.fetch()
# cursor.fetchSet()
# cursor.fetchone()
# cursor.fetchmany()
# cursor.fetchall()
# cursor.getSchema()
# cursor.next() - """ iterator-protocol for fetch next row. """
# cursor.getDatabases()
# cursor.close()

############################### pyhs2 API ###############################

import pyhs2
with pyhs2.connect(host='52.91.52.215',
                   port=10000,
                   authMechanism='PLAIN',
                   user='root',
                   #password='test',
                   database='default') as conn:

    with conn.cursor() as cur:
        #Show databases
        #print cur.getDatabases()

        #Execute query
        SQL = "select count(*) as cnt, primary_type from crimes group by primary_type"
        #SQL = "select * from e_streams limit 18"
        cur.execute(SQL)

        #Return column info from query
        #print cur.getSchema()

        #Fetch table results
        for i in cur.fetch():
            print i
