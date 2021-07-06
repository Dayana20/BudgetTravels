'''
Examples:
'https://pro.openweathermap.org/data/2.5/forecast/climate?q=London&appid={API key}'
'api.openweathermap.org/data/2.5/forecast/climate?q=London&cnt=3'
'api.openweathermap.org/data/2.5/forecast/climate?q=London&units=metric'

Nagpur, Nagpur District, Maharashtra, 440001, India
(21.1498134, 79.0820556)



'''

import requests
import json
from datetime import datetime


#city_name = input("City: ")
#country_code = generate_code(city_name)
API_key = 'ea395ebe708b1af005b17243cbc20ac9'
lat = '21.1498134'
lon = '79.0820556'
link = 'https://api.openweathermap.org/data/2.5/onecall?lat='+lat+'&lon='+lon+'&appid='+API_key
response = requests.get(link)
data = response.json()
for elem in data["daily"]:
    print(elem)
    
ts = int("1284101485")
print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))