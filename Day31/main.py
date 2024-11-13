import requests
import datetime as dt


# MY_LATITUDE = 43.653225
MY_LATITUDE = 20
# MY_LONGITUDE = -79.383186
MY_LONGITUDE = -175
MY_TIMEZONE = "Canada/Eastern"
SUNSET_URL = "https://api.sunrise-sunset.org/json"
ISS_URL = "http://api.open-notify.org/iss-now.json"


def get_iss_location():
    iss_response = requests.get(url=ISS_URL)
    iss_response.raise_for_status()
    iss_data = iss_response.json()    
    return float(iss_data["iss_position"]["latitude"]), float(iss_data["iss_position"]["longitude"])


def check_proximity(latitude, longitude):
    return (MY_LATITUDE - 5 <= latitude <= MY_LATITUDE + 5) and (MY_LONGITUDE - 5 <= longitude <= MY_LONGITUDE + 5)


params = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0,
    "tzid": MY_TIMEZONE,
}

response = requests.get(url=SUNSET_URL, params=params)
response.raise_for_status()
data = response.json()
sunset = dt.datetime.fromisoformat(data["results"]["sunset"]).time()
sunrise = dt.datetime.fromisoformat(data["results"]["sunrise"]).time()
print(f"{sunset=}")

current_time = dt.datetime.now().time()
print(f"{current_time=}")

if (current_time > sunset) or (current_time < sunrise):
    print("It's nighttime")
    # check for ISS
    iss_latitude, iss_longitude = get_iss_location()
    print(f"{iss_latitude=} {iss_longitude=}")
    print(check_proximity(iss_latitude, iss_longitude))
    