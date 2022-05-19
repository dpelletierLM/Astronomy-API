#!/usr/bin/env python3
import requests
import datetime
import json

ASTRONOMYAPI_ID="5afae862-243b-477b-bcf0-400cc33e5a1b"
ASTRONOMYAPI_SECRET="14ced2f1c9212a9ccdd014529be2c8e187c870889b8a28ca809b1162e24e77acd92664198e775dce7e7dcf8838f7c80ed340abb2415086ebbf5c359546099454a8dc2243e62a76dda64816be192d153f09128ba455ab5f2592b4478a28affec27a5e7ce24a1db719f04b76e7adfbf222
def get_observer_location():
    """Returns the longitude and latitude for the location of this machine.
    Returns:
    str: latitude
    str: longitude
    """
    response = requests.get("http://ip-api.com/json/18.206.10.123?fields=lat,lon")
    lat_lon = json.loads(response.text)
    latitude = lat_lon['lat']
    longitude = lat_lon['lon']

    # NOTE: Replace with your real return values!
    return latitude, longitude
    
def get_sun_position(latitude, longitude):
    """Returns the current position of the sun in the sky at the specified location
    
    Parameters:
    latitude (str)
    longitude (str)
    
    Returns:
    float: azimuth
    float: altitude
    """
    # NOTE: Replace with your real return values!
    return 0, 0
        
def print_position(azimuth, altitude):
    """Prints the position of the sun in the sky using the supplied coordinates
    
    Parameters:
    azimuth (float)
    altitude (float)
    """
    
    print("The Sun is currently at: ")
    
if __name__== "__main__":
    latitude, longitude = get_observer_location()
    azimuth, altitude = get_sun_position(latitude, longitude)
    print_position(azimuth, altitude)