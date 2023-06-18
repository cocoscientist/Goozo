import requests

def fetchLatest():
    r = requests.get('https://xkcd.com/info.0.json')
    return r.json()

def fetchByNum(x):
    r = requests.get(f'https://xkcd.com/{x}/info.0.json')
    return r.json()