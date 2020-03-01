"""
This is the user module and supports all the ReST actions for the
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
        #return PEOPLE
        URL = "https://bpdts-test-app.herokuapp.com/city/London/users"
        return get_people_json(URL)

    elif londonloc == "within50":
        london = (51.50853, -0.12574)
        maidstone = (51.272644, 0.525270)
        print("The distance between London and Maidstone is " + str(miles_from_london(maidstone)) + " miles")

def miles_from_london(coordinates):
    """
    This function takes latitude and longitude coordinates tuple as an argument.
    Geopy will calculate the distance the location is from London
    :return:        number miles distance from London
    """
    london_coordinates = (51.50853, -0.12574)
    miles = distance.great_circle(london_coordinates, coordinates).miles
    return miles