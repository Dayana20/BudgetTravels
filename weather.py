import requests
import json
from datetime import datetime
import pandas as pd
from pandas import DataFrame
import os
import sqlalchemy
from sqlalchemy import create_engine
from geopy.geocoders import Nominatim # pip install Nominatim and sudo pip install geopy 

city_name = input("City: ")
# get lat and lon from city name to use for weather api
geolocator = Nominatim(user_agent='myapplication')
location = geolocator.geocode(city_name)
print(location.address)# has all the raw info from city
lat = location.raw['lat']
lon = location.raw['lon']

API_key = 'ea395ebe708b1af005b17243cbc20ac9'
#lat = '21.1498134'
#lon = '79.0820556'
link = 'https://api.openweathermap.org/data/2.5/onecall?lat='+lat+'&lon='+lon+'&appid='+API_key+'&units=imperal'
response = requests.get(link)
data = response.json()
dt_temp = [] # dummy list
dic = {}
for elem in data["daily"]:
    #dt_format = str(datetime.utcfromtimestamp(elem["dt"]).strftime('%Y-%m-%d %H:%M:%S'))
    dt_format = str(datetime.utcfromtimestamp(elem["dt"]).strftime('%Y-%m-%d')) # not including the time
    # dt_temp.append([dt_format,elem["temp"]])
    # dt_temp.append(f'{dt_format},{elem["temp"]}')
    dic[dt_format] = elem["temp"]
    
    
# print(dic)

# print data in readable format from list
# for elem in dt_temp:
#     print(elem[0])
#     for key,value in elem[1].items():
#         if(key=="day"):
#             print("temp ", value)
#         else:
#             print(key,value)

# create dataframe
#col_Names =  ['date', 'temp', 'min', 'max', 'night', 'eve', 'mor']
info = pd.DataFrame.from_dict(dic, orient = 'index')
info = info.reset_index() ##includes index as a column and makes the index numbered
info = info.rename(columns={'index':'date','day':'temp'})
print(info)
print(info.columns)


# get started with the dataframe
# update
dbName = 'weather'
fileName = 'weather_file'
engine = create_engine('mysql://root:codio@localhost/' + dbName)
os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS ' + dbName + '; "')
os.system('mysql -u root -pcodio ' + dbName + ' < ' + fileName + '.sql')
tableName = 'weather_table'
df = pd.read_sql_table(tableName, con=engine)

# # write_table
os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '
              + dbName + '; "')
info.to_sql('weather_table', con=engine, if_exists='replace', index=False)

# #save data to fileName
info.to_sql('weather_table', con=engine, if_exists='replace', index=False)
os.system('mysqldump -u root -pcodio {} > {}.sql'.format(dbName, fileName))


