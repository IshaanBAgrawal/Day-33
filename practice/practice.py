import requests
from datetime import datetime

MY_LAT = 28.474388
MY_LNG = 77.503990

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# iss_position = (float(response.json()["iss_position"]["longitude"]), float(response.json()["iss_position"]["latitude"]))
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)

print(data["results"])

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
print(sunrise)

sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunset)

time_now = datetime.now()
print(time_now.hour)
