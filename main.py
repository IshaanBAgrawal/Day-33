import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

iss_position = (float(response.json()["iss_position"]["longitude"]), float(response.json()["iss_position"]["latitude"]))
print(iss_position)
