import smtplib
import random
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

# email authentication
APP_EMAIL = os.getenv("APP_EMAIL")
APP_PWD = os.getenv("APP_PWD")
TO_EMAIL = os.getenv("TO_EMAIL")

# read in the quotes file as a list
with open("Day32/quotes.txt") as f:
    quotes = f.readlines()

# details of email to send
email_subject = "Motivational Quote of the Day"
email_body = random.choice(quotes)
msg = f"Subject:{email_subject}\n\n{email_body}"

# get the current weekday
day_of_week = dt.date.today().weekday()

# if today is Monday, send an email with a motivational quote
if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=APP_EMAIL, password=APP_PWD)
        connection.sendmail(from_addr=APP_EMAIL, to_addrs=TO_EMAIL, msg=msg)
        print("Email sent.")
