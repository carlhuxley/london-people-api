import requests
import json
URL = "https://bpdts-test-app.herokuapp.com/users"
r = requests.get(URL)
j=r.json()
print(j)