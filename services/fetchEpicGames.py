import requests
from datetime import datetime

def fetchGames():
    allGames = requests.get('https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions').json()
    gameData = allGames['data']['Catalog']['searchStore']['elements']

    finalGameData = []

    for game in gameData:
        game_promotions = game['promotions']
        if game_promotions and not game_promotions['upcomingPromotionalOffers']:
            finalGameData.append(game)

    return finalGameData