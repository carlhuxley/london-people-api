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

# Data to serve with our API

URL = "https://bpdts-test-app.herokuapp.com/city/London/users"
r = requests.get(URL)
PEOPLE=r.json()

def read_london(londonloc):
    """
    This function responds to a request for /api/listed/londonuser
    with a lists of users listed as living in London or whose current 
    coordinates are within 50 miles of London
    :return:        json string of list of London users
    """
    #output users to console
    #URL = "https://bpdts-test-app.herokuapp.com/users"
    
    # Create the list of people from our data
    if londonloc == "listed":
        return PEOPLE
        


