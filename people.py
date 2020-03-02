"""
This is the people module and supports all the ReST actions for the
PEOPLE collection
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort
import requests
import json
from geopy.distance import geodesic
#from geopy import distance

def get_people_json(URL):
    """
    This function takes a URL as an argument and returns a
    json object from the https://bpdts-test-app.herokuapp.com/ API
    """
    r = requests.get(URL)
    return r.json()

def read_london(londonloc):
    """
    This function responds to a request for /api/listed/londonpeople
    with a lists of users listed as living in London or whose current 
    coordinates are within 50 miles of London
    :return:        json string of list of London users
    """
    
    if londonloc == "listed":
        # Return people listed as being located in London
        URL = "https://bpdts-test-app.herokuapp.com/city/London/users"
        return get_people_json(URL)

    elif londonloc == "within50":
        # Return people located within 50 miles of London
        URL = "https://bpdts-test-app.herokuapp.com/users"
        all_people = get_people_json(URL)

        # Create output dictionary of all people located within 50 miles of London
        output_dict = [x for x in all_people if miles_from_london((x['latitude'], x['longitude'])) <= 50]
        return output_dict

def miles_from_london(coordinates):
    """
    This function takes a latitude and longitude coordinates tuple as an argument.
    Geopy calculates the geodesic distance between two points.
    :return:        number miles distance from London
    """
    london_coordinates = (51.50853, -0.12574)
    miles = geodesic(london_coordinates, coordinates).miles
    return miles