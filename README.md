# London People ReST API
>A Flask API which returns people listed as living in London or people with geo-coordinates showing they live within 50 miles of London

## Installation

Linux:

Install program dependencies with pip requirements.txt
```sh
$ pip install -r requirements.txt
```

## Basic Usage

Start the Flask server with:
```sh
$ python server.py
```
## Swagger UI - API Testing
Start Swagger UI by going to http://localhost:5000/api/ui/ 

Using the 'listed' path parameter returns the following Response Body:
```sh
[
  {
    "email": "mboam3q@thetimes.co.uk",
    "first_name": "Mechelle",
    "id": 135,
    "ip_address": "113.71.242.187",
    "last_name": "Boam",
    "latitude": -6.5115909,
    "longitude": 105.652983
  },
  {
    "email": "tstowgillaz@webeden.co.uk",
    "first_name": "Terry",
    "id": 396,
    "ip_address": "143.190.50.240",
    "last_name": "Stowgill",
    "latitude": -6.7098551,
    "longitude": 111.3479498
  },
  {
    "email": "aseabrockeef@indiegogo.com",
    "first_name": "Andrew",
    "id": 520,
    "ip_address": "28.146.197.176",
    "last_name": "Seabrocke",
    "latitude": "27.69417",
    "longitude": "109.73583"
  },
  {
    "email": "smapstonei9@bandcamp.com",
    "first_name": "Stephen",
    "id": 658,
    "ip_address": "187.79.141.124",
    "last_name": "Mapstone",
    "latitude": -8.1844859,
    "longitude": 113.6680747
  },
  {
    "email": "tcolbertsonj3@vimeo.com",
    "first_name": "Tiffi",
    "id": 688,
    "ip_address": "141.49.93.0",
    "last_name": "Colbertson",
    "latitude": 37.13,
    "longitude": -84.08
  },
  {
    "email": "kgopsallm1@cam.ac.uk",
    "first_name": "Katee",
    "id": 794,
    "ip_address": "203.138.133.164",
    "last_name": "Gopsall",
    "latitude": 5.7204203,
    "longitude": 10.901604
  }
]
```
Using the 'within50' path parameter returns the following Response Body:
```sh
[
  {
    "email": "agarnsworthy7d@seattletimes.com",
    "first_name": "Ancell",
    "id": 266,
    "ip_address": "67.4.69.137",
    "last_name": "Garnsworthy",
    "latitude": 51.6553959,
    "longitude": 0.0572553
  },
  {
    "email": "hlynd8x@merriam-webster.com",
    "first_name": "Hugo",
    "id": 322,
    "ip_address": "109.0.153.166",
    "last_name": "Lynd",
    "latitude": 51.6710832,
    "longitude": 0.8078532
  },
  {
    "email": "phebbsfd@umn.edu",
    "first_name": "Phyllys",
    "id": 554,
    "ip_address": "100.89.186.13",
    "last_name": "Hebbs",
    "latitude": 51.5489435,
    "longitude": 0.3860497
  }
]
```
