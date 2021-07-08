import requests
import json
from datetime import datetime
import pandas as pd
from pandas import DataFrame
import os
import sqlalchemy
from sqlalchemy import create_engine
from geopy.geocoders import Nominatim # pip install Nominatim and sudo pip install geopy 
import matplotlib.pyplot as plt

def get_data_w(city_name):
    # get lat and lon from city name to use for weather api
    geolocator = Nominatim(user_agent='myapplication')
    location = geolocator.geocode(city_name)
    print(location.address)# has all the raw info from city
    lat = location.raw['lat']
    lon = location.raw['lon']
    return lat,lon,location


def set_up_w(lat,lon,API_key):
    link = 'https://api.openweathermap.org/data/2.5/onecall?lat='+lat+'&lon='+lon+'&appid='+API_key+'&units=imperial'
    response = requests.get(link)
    data = response.json()
    dt = [] # week
    dic = {}
    for elem in data["daily"]:
        #dt_format = str(datetime.utcfromtimestamp(elem["dt"]).strftime('%Y-%m-%d %H:%M:%S'))
        dt_format = str(datetime.utcfromtimestamp(elem["dt"]).strftime('%Y-%m-%d')) # not including the time
        dt.append(str(datetime.utcfromtimestamp(elem["dt"]).strftime('%m/%d')))
        # dt_temp.append([dt_format,elem["temp"]])
        # dt_temp.append(f'{dt_format},{elem["temp"]}')
        dic[dt_format] = elem["temp"]
    return dic


# create dataframe
def create_dataframe_w(dic):
    #col_Names =  ['date', 'temp', 'min', 'max', 'night', 'eve', 'mor']
    info = pd.DataFrame.from_dict(dic, orient = 'index')
    info = info.reset_index() ##includes index as a column and makes the index numbered
    info = info.rename(columns={'index':'date','day':'temp'})
    print(info)
    # print(info.columns)
    return info

# get started with the dataframe
# update
def update_w(dbName, fileName, tableName, info):
    engine = create_engine('mysql://root:codio@localhost/' + dbName)
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS ' + dbName + '; "')
    os.system('mysql -u root -pcodio ' + dbName + ' < ' + fileName + '.sql')

    info.to_sql(tableName, con=engine, if_exists='replace', index=False)
    df = pd.read_sql_table(tableName, con=engine)
    return df, engine


# write_table
def write_table_w(dbName,engine,info):
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '
                  + dbName + '; "')
    info.to_sql('weather_table', con=engine, if_exists='replace', index=False)
    #print(engine.execute("SELECT * FROM "+tableName).fetchall()) #should print

# #save data to fileName
def save_data_w(dbName, fileName, engine,info):
    info.to_sql('weather_table', con=engine, if_exists='replace', index=False)
    os.system('mysqldump -u root -pcodio {} > {}.sql'.format(dbName, fileName))

def main():
    city_name = input("City: ")
    lat, lon, location = get_data(city_name)
    API_key = 'ea395ebe708b1af005b17243cbc20ac9'
    dic = set_up(lat,lon,API_key)
    info = create_dataframe(dic)
    dbName = 'weather'
    fileName = 'weather_file'
    tableName = 'weather_table'
    df, engine = update(dbName, fileName, tableName, info)
    write_table(dbName,engine, info)
    save_data(dbName, fileName, engine,info)
    
    # visualiation
    df.plot.bar(x='date', y='temp')
    plt.title(location.address)
    plt.savefig('weather_bar.png')
    
# main()