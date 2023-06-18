import requests

def getRandomFact():
    return requests.get('https://uselessfacts.jsph.pl/api/v2/facts/random?language=en').json()