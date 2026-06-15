import requests
import json

quotes = requests.get(url='https://api.kanye.rest/')
quotes.raise_for_status()

Kanye = quotes.json()
print(Kanye)