import json
import pyowm
import geonamescache
import re
from curses import ascii
import string

import time
import psycopg2

def isAscii(s):
    for c in s:
        if c not in string.ascii_letters:
            return False
    return True

gc = geonamescache.GeonamesCache()
cities = gc.get_cities()

weather = {}
finaldict = {}
owm = pyowm.OWM('b4d6a45357444bb50ea559bb93971d50')
conn = psycopg2.connect(user="postgres", password="pass", host="localhost", port="5432")
for i in cities:
    print cities[i]['name']
    if isAscii(cities[i]['name']) == True:
           weather = {} 
           observation = owm.weather_at_place(cities[i]['name'])
           w = observation.get_weather()
           weather['city'] = cities[i]['name']
           weather['date'] = time.strftime("%d/%m/%Y")
           temp = w.get_temperature('celsius')
           weather['temp_lo'] = temp['temp_min']
           weather['temp_hi'] = temp['temp_max']
           weather['temp']=temp['temp']
           weather['pressure']= w.get_pressure()
           weather['wind']= w.get_wind()
           weather['snow']=w.get_snow()
           weather['rain']=w.get_rain()
           weather['sunrise_time']=w.get_sunrise_time()
           weather['sunset_time']=w.get_sunset_time()
           weather['status']=w.get_detailed_status()
           weather['weather_cd']=w.get_weather_code()
           weather['visibility_distance']=w.get_visibility_distance()
           weather['dewpoint']=w.get_dewpoint()
           weather['humidity']=w.get_humidity()
           finaldict.update(weather)
           query =  "INSERT INTO weather(city,date,temp_lo,temp_hi,temp,pressure,wind,snow,rain,\
                   sunrise_time,sunset_time,status,weather_cd,visibility_distance,dewpoint,humidity)\
                   VALUES (%s, %s, %s,%s,%s, %s, %s,%s,%s, %s, %s,%s,%s, %s, %s,%s);"
           data = (weather['city'] , weather['date'] , weather['temp_lo'],\
                   weather['temp_hi'] ,weather['temp'],weather['pressure'],weather['wind'],weather['snow'],weather['rain'],\
                   weather['sunrise_time'],weather['sunset_time'],weather['status'],weather['weather_cd'],weather['visibility_distance'],\
                   weather['dewpoint'],\
                   weather['humidity'])

           cursor = conn.cursor()
           cursor.execute(query, data)
           conn.commit()
    
           
    else:
          print 'Not a ascii city:',cities[i]['name']
          break


 
 
   
