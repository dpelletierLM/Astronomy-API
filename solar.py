#!/usr/bin/env python3
import requests
import json
from datetime import datetime, date
from_date = date.today()
to_date = date.today()
timenow = datetime.now()
current_time = timenow.strftime("%H:%M:%S")


ASTRONOMYAPI_ID = "5afae862-243b-477b-bcf0-400cc33e5a1b"
ASTRONOMYAPI_SECRET = "14ced2f1c9212a9ccdd014529be2c8e187c870889b8a28ca809b1162e24e77acd92664198e775dce7e7dcf8838f7c80ed340abb2415086ebbf5c359546099454a8dc2243e62a76dda64816be192d153f09128ba455ab5f2592b4478a28affec27a5e7ce24a1db719f04b76e7adfbf222"
def get_observer_location():
    """Returns the longitude and latitude for the location of this machine.
    Returns:
    str: latitude
    str: longitude
    """
    location_url = "http://ip-api.com/json?fields=lat,lon"
    response = requests.get(location_url)
    #response = requests.get('http://ip-api.com/json/18.206.10.123?fields=lat,lon')
    lat_lon = response.json()
    latitude = lat_lon['lat']
    longitude = lat_lon['lon']

    # NOTE: Replace with your real return values!
    print(latitude,longitude)
    return latitude, longitude

def get_elevation(latitude,longitude): # Gets elevation from latitude and longitude 
    elev_url = "https://api.open-elevation.com/api/v1/lookup?locations={0},{1}".format(
        latitude,
        longitude,
        )
    elev_response = requests.get(elev_url)
    elev_response_data = elev_response.json()
    elevation = elev_response_data["results"][0]["elevation"]
    print(elevation)
    return elevation
    
def get_sun_position(latitude, longitude, elevation):
    """Returns the current position of the sun in the sky at the specified location"""
    
    sun_payload = {
        "latitude": latitude,
        "longitude": longitude,
        "elevation": elevation,
        "time": current_time,
        "from_date": from_date,
        "to_date": to_date,
    }

    sun_response = requests.get(
        "https://api.astronomyapi.com/api/v2/bodies/postion/sun?", 
        params=sun_payload,
        auth=(ASTRONOMYAPI_ID, ASTRONOMYAPI_SECRET),
    )

    sun_response_data = sun_response.json()
    print(sun_response_data)
    
    sun_1 = sun_response_data["data"]["table"]["rows"][0]["cells"][0]["position"]["horizontal"]

    azimuth = sun_1["azimuth"]["degrees"]
    altitude = sun_1["altitude"]["degrees"]
    return azimuth, altitude
        
def print_position(azimuth, altitude):
    """Prints the position of the sun in the sky using the supplied coordinates
    
    Parameters:
    azimuth (float)
    altitude (float)
    """
    
    
    print("The Sun is currently at: ", azimuth, altitude)
    
if __name__== "__main__":
    latitude, longitude = get_observer_location()
    elevation = get_elevation(latitude,longitude)
    azimuth, altitude = get_sun_position(latitude, longitude, elevation)
    print_position(azimuth, altitude)