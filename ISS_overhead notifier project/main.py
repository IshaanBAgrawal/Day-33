import requests
from datetime import datetime
import smtplib
import time

# Your latitude
MY_LAT = 28.474388
# Your longitude
MY_LONG = 77.503990
MY_DETAILS = {
    "E-MAIL": "kanha123app@gmail.com",
    "PASS": "1234ishaan",
}


def lat_long_check():
    iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss.raise_for_status()
    iss_data = iss.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    lat_condition = MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
    long_condition = MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    if lat_condition and long_condition:
        return True
    else:
        return False

# Your position is within +5 or -5 degrees of the ISS position.


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    sunrise_or_sunset = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sunrise_or_sunset.raise_for_status()
    sunrise_sunset_data = sunrise_or_sunset.json()

    sunrise = int(sunrise_sunset_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sunrise_sunset_data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour

    if sunset < hour_now < sunrise:
        return True
    else:
        return False


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if lat_long_check() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_DETAILS["E-MAIL"], password=MY_DETAILS["PASS"])
            connection.sendmail(
                from_addr=MY_DETAILS["E-MAIL"],
                to_addrs="agrawalishaan115@gmail.com",
                msg="Subject:LOOK UP!\n\nThe ISS is just above your head. Loo up to get it's amazing view!"
            )
