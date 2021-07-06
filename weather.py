import requests
import json
from datetime import datetime
from geopy.geocoders import Nominatim # pip install Nominatim and sudo pip install geopy 

city_name = input("City: ")

# get lat and lon from city name to use for weather api
geolocator = Nominatim(user_agent='myapplication')
location = geolocator.geocode("Guayaquil")
print(location.address)# has all the raw info from city
lat = location.raw['lat']
lon = location.raw['lon']

API_key = 'ea395ebe708b1af005b17243cbc20ac9'
#lat = '21.1498134'
#lon = '79.0820556'
link = 'https://api.openweathermap.org/data/2.5/onecall?lat='+lat+'&lon='+lon+'&appid='+API_key+'&units=imperal'
response = requests.get(link)
data = response.json()
dt = []
temp = []
dt_temp = []
for elem in data["daily"]:
    dt_format = str(datetime.utcfromtimestamp(elem["dt"]).strftime('%Y-%m-%d %H:%M:%S'))
    dt.append(dt_format)
    temp.append(elem["temp"])
    dt_temp.append(f'{dt_format},{elem["temp"]}')

for elem in dt_temp:
    print(elem)