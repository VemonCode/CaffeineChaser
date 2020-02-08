# CaffeineChaser
Working on a project that shows me the nearest coffee shops.

Note that in the details.json file, any thing that is all-caps, is user identified. Mainly because I don't want to leak my adress and API key. 

You can get your API Key by going to https://console.cloud.google.com/ and making a project. Copy the API key.

"LOCATION_LATITUDE" is your locations latitude, and "LOCATION_LONGITUDE" is your locations longitude. You can get your location LA and LO from Google Maps, searching your location, right clicking the pin point thing, and selecting "What's Here?". Down in the bottom, it'll say something like "11.111, 22.222". Put that in the "location" variable link, but no space. Example:

location=11.111,22.222

For the python file, I'm using the Requests library, which you can install by going into a terminal and entering "pip install requests".
Documentation for Requests: https://requests.readthedocs.io/en/master/
