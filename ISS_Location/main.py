import requests
import json
response = requests.get(url = 'http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data = response.json()
long = data['iss_position']['longitude']
lati = data['iss_position']['latitude']

iss_pos = (lati,long)
print(iss_pos)