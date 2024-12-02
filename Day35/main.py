import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

OWM_URL = 'https://api.openweathermap.org/data/2.5/forecast'
MY_LAT = 43.653225
MY_LONG = -79.383186
API_KEY = os.getenv("API_KEY")

params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "units": "metric",
    "appid": API_KEY
}

# access the openweathermap.org 5-day forecast
response = requests.get(url=OWM_URL, params=params)
response.raise_for_status()
data = response.json()

# get each of the temperature readings and print
for reading in data['list']:
    local_time = dt.datetime.fromtimestamp(reading['dt'])
    utc_time = reading['dt_txt']
    temperature = reading['main']['temp']
    weather = reading['weather'][0]['description']
    print(f"Local Time: {local_time}\nUTC Time: {utc_time}\nTemperature: {temperature} C\nWeather: {weather}\n")
