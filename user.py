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



def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API

#print(PEOPLE)


def read_london():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        json string of list of people
    """
    #output users to console
    #URL = "https://bpdts-test-app.herokuapp.com/users"
    URL = "https://bpdts-test-app.herokuapp.com/city/London/users"
    r = requests.get(URL)
    PEOPLE=r.json()
    print (PEOPLE)
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.key())]


