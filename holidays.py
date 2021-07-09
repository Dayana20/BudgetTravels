import requests
import json
from datetime import datetime
import pandas as pd
from pandas import DataFrame
import os
import sqlalchemy
from sqlalchemy import create_engine

def get_api():
    #country = input('Enter country name: ')
    api_key = 'AIzaSyCwSZgFVPsjmPIVyQYoOV595zIVdfwU7oQ'
    return api_key


def build_url(country, api_key):
    return 'https://www.googleapis.com/calendar/v3/calendars/en.' + country + '%23holiday%40group.v.calendar.google.com/events?key=' + api_key


# get json from url
def get_json(url):
    response = requests.get(url)
    #print(response) # added this
    return response.json()


# build useful dictionary from json
def build_dict(json):
    holiday_dict = {}
    for holiday in json['items']:
        holiday_dict[holiday['summary']]= {holiday['start']['date'], holiday['end']['date']}
    return holiday_dict


def build_dataframe(dic):
    #dic = build_dict(json)
    # creating dataframe from dictionary
    holiday_df = pd.DataFrame.from_dict(dic, orient = 'index', columns = ['start_date', 'end_date'])
    holiday_df = holiday_df.reset_index()
    holiday_df = holiday_df.rename(columns = {'index': 'holiday'})
    return holiday_df


def write_table_h(dataframe, dbName, tableName, engine):
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '
              + dbName + '; "')
    dataframe.to_sql(tableName, con=engine, if_exists='replace', index=False)

    
def save_data_to_file(dataframe, dbName, tableName, fileName, engine):
    dataframe.to_sql(tableName, con=engine, if_exists='replace', index=False)
    os.system('mysqldump -u root -pcodio {} > {}.sql'.format(dbName, fileName))
    

def load_database(dbName, fileName):
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS ' + dbName + '; "')
    os.system('mysql -u root -pcodio ' + dbName + ' < ' + fileName + '.sql')
    
    
def update_database(dbName, tableName, fileName, engine):
    load_database(dbName, fileName)
    df = pd.read_sql_table(tableName, con=engine)
    return df

def main():
    country_name = 'uk'
    api_key = get_api()
    url = build_url(country_name, api_key) # moved this up here
    json = get_json(url)
    # print(json)
    dic = build_dict(json)
#     print(dic)
    df = build_dataframe(dic)
    print(df)
    
    
    
# if __name__ == "__main__":
#     main()


#holiday_df.to_sql(tableName, con=engine, if_exists='replace', index=False)




