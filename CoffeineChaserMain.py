import requests
import json

# I want to fucking die

shittyRequest = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?type=cafe&location=LOCATION_LATITUDE,LOCATION_LONGTITUDE&radius=2500&key=YOUR_API_KEY")

data = shittyRequest.json()["results"]
for result in data:
  print(result["name"] + result["location"] + result["opening_hours"] + result["open_now"])
