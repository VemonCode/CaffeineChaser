import requests
import warnings

# I want to fucking die

shittyRequest = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?type=cafe&location=LOCATION_LATITUDE,LOCATION_LONGITUDE&radius=2500&key=YOUR_API_KEY")
print(shittyRequest)
