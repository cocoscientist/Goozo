import requests

def fetchLatest():
    r = requests.get('https://xkcd.com/info.0.json')
    return r.json()

def fetchByNum(x):
    maxNum = requests.get('https://xkcd.com/info.0.json').json()['num']
    r = None
    if x==404 or maxNum<x or x<1:
        r = {"month": "4", "num": 404, "link": "", "year": "2008", "news": "", "safe_title": "Error 404", "transcript": "", "alt": "It's 'cause you're dumb.", "img": "https://www.explainxkcd.com/wiki/images/9/92/not_found.png", "title": "Error 404", "day": "1"}
    else:
        r = requests.get(f'https://xkcd.com/{x}/info.0.json').json()
    return r