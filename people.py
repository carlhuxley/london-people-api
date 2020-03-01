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
import geopy
from geopy import distance

# Data to serve with our API

def get_people_json(URL):
    """
    This function takes a URL as an argument and returns a
    json object from the https://bpdts-test-app.herokuapp.com/ API
    """
    r = requests.get(URL)
    return r.json()

#URL = "https://bpdts-test-app.herokuapp.com/users"

def read_london(londonloc):
    """
    This function responds to a request for /api/listed/londonpeople
    with a lists of users listed as living in London or whose current 
    coordinates are within 50 miles of London
    :return:        json string of list of London users
    """
    
    # Create the list of people from our data
    if londonloc == "listed":
        #return people listed as being located in London
        URL = "https://bpdts-test-app.herokuapp.com/city/London/users"
        return get_people_json(URL)

    elif londonloc == "within50":
        #return people located within 50 miles of London
        URL = "https://bpdts-test-app.herokuapp.com/users"
        all_people = get_people_json(URL)

        # Filter python objects with list comprehensions
        output_dict = [x for x in all_people if miles_from_london((x['latitude'], x['longitude'])) <= 50]
        return output_dict

def miles_from_london(coordinates):
    """
    This function takes latitude and longitude coordinates tuple as an argument.
    Geopy will calculate the distance the location is from London
    :return:        number miles distance from London
    """
    london_coordinates = (51.50853, -0.12574)
    miles = distance.great_circle(london_coordinates, coordinates).miles
    return miles