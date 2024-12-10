#!/usr/bin/python3
# Script to fetch the temperature and other info of a city from weather app
import requests
import json
from datetime import datetime

def time_from_utc_with_timezone(utc_with_tz):
    from datetime import timezone
    local_time = datetime.fromtimestamp(utc_with_tz, tz=timezone.utc)
    return local_time.time()
    
# asking the user for api key
 api_key = input("Please Enter Your API: ")

#asking the user for city name
city_name = input("Please Enter Your City Name: ")

# Get the time from utc and timezone values provided
# pass the value as utc + timezone (both are UTC timestamp)

# API url
weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key

# Get the response from weather url
response = requests.get(weather_url)

# response will be in json format and we need to change it to pythonic format
weather_data = response.json()

if weather_data['cod'] == 200:
    kelvin = 373.15 # Temperature shown here is in Kelvin and I will show in Celsius
    temp = int(weather_data['main']['temp'] - kelvin)
    feels_like_temp = int(weather_data['main']['feels_like'] - kelvin)
    pressure = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed'] * 3.6
    print(f"Weather Information for City: {city_name}")
    print(f"Temperature (Celsius): {temp}")
    print(f"Feels like in (Celsius): {feels_like_temp}")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    
    description = weather_data['weather'][0]['description']
    sunrise_time = time_from_utc_with_timezone(sunrise + timezone)
    sunset_time = time_from_utc_with_timezone(sunset + timezone)
    print("Wind speed: {0:.2f} km/hr".format(wind_speed))

    
    sunrise = weather_data['sys']['sunrise']
    sunset = weather_data['sys']['sunset']
    timezone = weather_data['timezone']
    cloudy = weather_data['clouds']['all']
    print(f"Sunrise at {sunrise_time} and Sunset at {sunset_time}")
    print(f"Cloud: {cloudy}%")
    print(f"Info: {description}")
else:
    print(f"City Name: {city_name} was not found!")


