import urllib.request #opens http url
import json  #imports json package
import time

def location_weather(): #defines the function

  url = 'http://api.open-notify.org/iss-now.json'

  response = urllib.request.urlopen(url)
  result = json.loads(response.read())

  lat = result["iss_position"]["latitude"] #retrieves the latitude value from dictionary and store in the variable
  lon = result["iss_position"]["longitude"] #retrieves the longitude value from dictionary and store in the variable
  print (lat,lon)
  
