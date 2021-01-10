# This is the script designed to call open weather api to return .csv data for analysis
# Dependencies and Setup
import pandas as pd
import numpy as np
import requests
import time
import json


# Import API key
from open_w import api_key

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)
# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(lat_range[0], lat_range[1], size=1500)
lngs = np.random.uniform(lng_range[0], lng_range[1], size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
print (f'Citipy found {len(cities)} cities to dial')

#In this cell my goal is to build an api call to openweather api 
#This is my test case for London
#need Max Temp, humidity%, cloudiness%, windspeed, country code, date, name, latitude and longitude 

#assembling call url and making test call

base_url = "http://api.openweathermap.org/data/2.5/weather?q="

test_city = "London"

url = f'{base_url}{test_city}&appid={api_key}'

response = requests.get(url)

weather = response.json()

#Notes from json entry: entry is a dict
#key 'coord' returns a dict 'lat'  is key for latitude, 'lon' is key for longitude
#key 'name' returns name
#key 'wind' returns a dict 'speed' returns wind speed value
#key 'clouds' returns a dict 'all' returns the value
#key 'main' returns a dictionary with most of the data of interest: 'temp' calls temp (in K),
#     'humidity' returns humidity, 'temp_max' returns max temp
#key 'dt' returns the date
#key 'sys' returns a dict, 'country' returns a country code

#this is a test to make sure the api can be reached

try:
    #calling some dict keys from the json object returned by the call
    wspeed = float(weather['wind']['speed'])

    temp_c = float(weather['main']['temp']) - 273.15

    humid = float(weather['main']['humidity'])

    c_cover = float(weather['clouds']['all'])

    #test output
    print('London Weather')
    print(f'Temperature is {temp_c} degrees celsius')
    print(f'Wind speed is {wspeed} m/s')
    print(f'Relative humidity is {humid} percent')
    print(f'Cloud cover is {c_cover} percent')
    print(f'------------------------ \n')

except:
    print(f'The application failed to reach London, qutting...')
    quit()


#set up lists for data

#dates
dates = []

#city names
c_names = []

#country code
c_codes = []

#latitude coordinate
lats = []

#longitude coordinate
lons = []

#max temperature
m_temp = []

#max temp fahrenheit
f_temp = []

#cloudiness
c_covs = []

#humidity
hums = []

#wind speed
wnd = []


#start of the for loop
for city in cities:

    #construct a url using the current city from list cities
    iurl = f'{base_url}{city}&appid={api_key}'
    
    #call the api and request a response
    output = requests.get(iurl)
    
    #convert output to a json format
    w_data = output.json()
    
    #try to append data to the lists
    
    try:
        #append commands to store data in lists
        dates.append(w_data['dt'])
        c_names.append(w_data['name'])
        c_codes.append(w_data['sys']['country'])
        lats.append(float(w_data['coord']['lat']))
        lons.append(float(w_data['coord']['lon']))
        m_temp.append(float(w_data['main']['temp_max'] - 273.15))
        f_temp.append(float((w_data['main']['temp_max'] - 273.15)*1.8 + 32))
        c_covs.append(float(w_data['clouds']['all']))
        hums.append(float(w_data['main']['humidity']))
        wnd.append(float(w_data['wind']['speed']))
        
        #output statement to confirm success
        print(f'Data from {city} stored in memory')
        
    except:
        
        #output statement for failure case
        print(f'Call failed for {city}')
        
    #line to tell the loop to allow a little time before the next call
    #this comes from the time module and tells it to sleep for however long it took to get a response
    time.sleep(output.elapsed.total_seconds())

print(f'------------------------\n')       
print(f'Finished receiving weather data')
print(f'Dialer recieved values from {len(c_names)} weather stations') 
print(f'------------------------\n')   

#write weather data to a dataframe
w_dict = {'city_name': c_names, 'country':c_codes, 'date': dates, 'lat':lats, 'lon':lons, 'max_temp_C': m_temp,
         'max_temp_F':f_temp, 'cloud_cover%': c_covs, 'humidity%': hums, 'wind_speed': wnd}

w_df = pd.DataFrame(w_dict)

name = input('enter the date in format: mm_dd_yy: ')

w_df.to_csv(f'global_weather_survey_{name}.csv', index = False)

print('File written, closing down')

quit()

