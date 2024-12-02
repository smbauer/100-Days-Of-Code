import requests
import datetime as dt
from smtplib import SMTP
import time
import os
from dotenv import load_dotenv

load_dotenv()

# current location parameters
MY_LAT = float(os.getenv("MY_LAT"))
MY_LONG = float(os.getenv("MY_LONG"))
MY_TIMEZONE = "Canada/Eastern"
# website urls
SUNSET_URL = "https://api.sunrise-sunset.org/json"
ISS_URL = "http://api.open-notify.org/iss-now.json"
# email authentication
APP_EMAIL = os.getenv("APP_EMAIL")
APP_PWD = os.getenv("APP_PWD")
TO_EMAIL = os.getenv("TO_EMAIL")


def is_iss_overhead():
    '''Gets the current location of the ISS and returns True if it's overhead'''
    iss_response = requests.get(url=ISS_URL)
    iss_response.raise_for_status()
    iss_data = iss_response.json()    
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    return (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)


def is_night():
    '''Get the sunrise/sunset times for my current location and returns True if it's night time'''    
    params = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": MY_TIMEZONE,
    }

    response = requests.get(url=SUNSET_URL, params=params)
    response.raise_for_status()
    data = response.json()
    sunset = dt.datetime.fromisoformat(data["results"]["sunset"]).time()
    sunrise = dt.datetime.fromisoformat(data["results"]["sunrise"]).time()
    current_time = dt.datetime.now().time()

    return (current_time > sunset) or (current_time < sunrise)


def send_email(to_email, msg):
    '''Send an email msg to a specified email address'''
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=APP_EMAIL, password=APP_PWD)
        connection.sendmail(from_addr=APP_EMAIL, to_addrs=to_email, msg=msg)

# use loop to check continuously
# while True:
if is_night() and is_iss_overhead():
    # ISS is overhead, send email notification
    msg = f"Subject: Look up!\n\nThe ISS is currently overhead."
    send_email(to_email=TO_EMAIL, msg=msg)
else:
    print("not overhead")
    # time.sleep(60)
