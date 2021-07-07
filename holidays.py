import requests
import json
from datetime import datetime
import pandas as pd
from pandas import DataFrame
import os
import sqlalchemy
from sqlalchemy import create_engine

api_key = 'AIzaSyCwSZgFVPsjmPIVyQYoOV595zIVdfwU7oQ'
country = input('Enter country name: ')

url = 'https://www.googleapis.com/calendar/v3/calendars/en.' + country + '%23holiday%40group.v.calendar.google.com/events?key=' + api_key

response = requests.get(url)
data = response.json()
# print(data)
holiday_dict = {}
for holiday in data['items']:
    # print(holiday["summary"])
    holiday_dict[holiday['summary']]= {holiday['start']['date'], holiday['end']['date']}
    
# print(holiday_dict)

holiday_df = pd.DataFrame.from_dict(holiday_dict, orient = 'index', columns = ['start_date', 'end_date'])
holiday_df = holiday_df.reset_index()
#print(holiday_df.columns)
holiday_df = holiday_df.rename(columns = {'index': 'holiday'})
print(holiday_df)

# get started with the dataframe
# update
dbName = 'holidays'
fileName = 'holiday_file'
tableName = 'holiday_table'
engine = create_engine('mysql://root:codio@localhost/' + dbName)
os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS ' + dbName + '; "')
os.system('mysql -u root -pcodio ' + dbName + ' < ' + fileName + '.sql')

holiday_df.to_sql(tableName, con=engine, if_exists='replace', index=False)
df = pd.read_sql_table(tableName, con=engine)

# # write_table
os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '
              + dbName + '; "')

holiday_df.to_sql(tableName, con=engine, if_exists='replace', index=False)
print(engine.execute("SELECT * FROM "+tableName).fetchall()) ##not working

# #save data to fileName
holiday_df.to_sql(tableName, con=engine, if_exists='replace', index=False)
os.system('mysqldump -u root -pcodio {} > {}.sql'.format(dbName, fileName))

