
import pyhs2
import psycopg2

hv_conn = pyhs2.connect(host='localhost', port=10000, authMechanism="PLAIN", user='root', database='default')
hv_cur = hv_conn.cursor()
pg_conn = psycopg2.connect(database="strava", user="postgres", password="pass", host="localhost", port="5432")
pg_cur = pg_conn.cursor()

# 1. get the popular segments
print 'selecting popular segments...'
hql = 'from ( select rank() over (partition by state,category order by effort_count desc) as rank, \
    effort_count as cnt, city, state, category, name, id, distance \
  from m_segment ) t_rank select rank, cnt, city, state, category, distance, id, name where rank <= 30'

hv_cur.execute(hql)
for r in hv_cur.fetch():
    pg_cur.execute("INSERT INTO segment VALUES (%s,%s,%s,%s,%s,%s,%s)", (r[6],r[7],r[2],r[3],r[4],r[5],r[1]))

pg_conn.commit()

# 2. get the leaderboard for popular segments
print 'Populating leaderboard for popular segments...'
hql = 'from ( from ( select rank() over (partition by state,category order by effort_count desc) as rank, \
      effort_count as cnt, state, category, name, id from m_segment ) t_rank \
  select rank, cnt, state, category, id, name where rank <=30 ) pop \
left join m_leaderboard l on pop.id=l.seg_id select pop.id as seg_id,  pop.name,  l.athlete_name,  \
l.athlete_gender,  l.moving_time,  l.rank,  l.average_hr, l.average_watts, l.effort_id, l.elapsed_time'

hv_cur.execute(hql)
for r in hv_cur.fetch():
    pg_cur.execute("INSERT INTO leaderboard VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (r[0],r[5],r[6],r[7],r[8],r[2],r[3],r[4],r[9]))

pg_conn.commit()

# 3. get the stream data for popular segments
print 'Populating altitude for popular segments...'
hql = 'from ( from (  select rank() over (partition by state,category order by effort_count desc) as rank, \
    effort_count as cnt,    state,    category,    name,    id   from m_segment) t_rank \
select rank, cnt, state, category, id, name where rank <=30 \
) pop left join m_stream s on pop.id=s.seg_id select pop.id as seg_id, s.distance, s.altitude'

hv_cur.execute(hql)
for r in hv_cur.fetch():
    pg_cur.execute("INSERT INTO stream VALUES (%s,%s,%s)", (r[0],r[1],r[2]))

pg_conn.commit()

# shot down connections for both
hv_cur.close()
hv_conn.close()
pg_cur.close()
pg_conn.close()

print 'Job completed!'
