import requests

def getCoffee():
    return requests.get('https://coffee.alexflipnote.dev/random.json').json()