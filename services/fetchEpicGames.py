import requests
from datetime import datetime

def fetchGames():
    allGames = requests.get('https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions').json()
    gameData = allGames['data']['Catalog']['searchStore']['elements']

    finalGameData = []

    for game in gameData:
        game_promotions = game['promotions']
        finalInsertion = {}
        if game_promotions and not game_promotions['upcomingPromotionalOffers']:
            finalInsertion['title'] = game['title']
            finalInsertion['desc'] = game['description']
            finalInsertion['publisher'] = game['seller']['name']

            gameImg = None
            for image in game['keyImages']:
                if image['type'] == 'OfferImageWide':
                    gameImg = image['url']
            finalInsertion['image'] = gameImg

            finalInsertion['url'] = f"https://store.epicgames.com/fr/p/{game['catalogNs']['mappings'][0]['pageSlug']}"

            finalGameData.append(finalInsertion)

    return finalGameData

def currentGameData(itemNo:int):
    allGamesData = fetchGames()
    length = len(allGamesData)
    if itemNo<=0:
        itemNo = 1
    elif itemNo>length:
        itemNo = length

    gameData = allGamesData[itemNo-1]

    gameData['dates'] = f"Item {itemNo} of {length}"
    return gameData