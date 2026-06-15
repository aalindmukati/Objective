import requests
import json
response = requests.get(url = 'http://api.open-notify.org/iss-ngiow.json')
response.raise_for_status()