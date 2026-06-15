import requests
import json

def quoates():
    quotes = requests.get(url='https://api.kanye.rest/')
    quotes.raise_for_status()

    Kanye = quotes.json()
    print("---------------")
    print(Kanye)

a = input('Do you want a quote (yes) or (no) ').lower()

if a == 'yes':
    quoates()
else:
    print('Goodbye to the sun that shines for me no longer.')