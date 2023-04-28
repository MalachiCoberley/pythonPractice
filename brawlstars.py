#ya boi plays too much brawlstars, so i'm going to practice with the API.

import urllib3
import json

from api_keys import TEST_API_TOKEN
from brawl_utils import calculate_showdown_result, is_showdown

MAL_URL = '%2328RP22UYC'
MAL_PLAIN = '#28RP22UYC'
CAL_URL = '%2320CL0P8C0'
CAL_PLAIN = '#20CL0P8C0'
http = urllib3.PoolManager()

headers = {'Authorization': f'Bearer {TEST_API_TOKEN}'}
url = f'https://api.brawlstars.com/v1/players/{MAL_URL}/battlelog'

resp = http.request('GET', url, headers=headers)
jason = json.loads(resp.data)

#iterate through each match to fetch needed info
#TODO: may need to account for other non-standard matches like weekend-only modes.
for match in jason['items']:
    timestamp = match['battleTime']
    game_mode = match['battle']['mode']
    result = ""
    star_player = False
    brawler = ""
    if is_showdown(game_mode):
        result = calculate_showdown_result(game_mode, match['battle']['rank'])
        if game_mode == "soloShowdown":
            for player in match['battle']['players']:
                if player["tag"] == MAL_PLAIN:
                            brawler = player['brawler']['name']
        else:
            while brawler == "":
                for team in match['battle']['teams']:
                    for player in team:
                        if player["tag"] == MAL_PLAIN:
                            brawler = player['brawler']['name']
    #For duels, I'm just grabbing the first brawler. The info for this mode kind of sucks.
    elif game_mode == "duels":
        result = match['battle']['result']
        for player in match['battle']['players']:
                if player["tag"] == MAL_PLAIN:
                            brawler = player['brawlers'][0]['name']
    else:
        result = match['battle']['result']
        if match['battle']['starPlayer']['tag'] == MAL_PLAIN:
            star_player = True
            brawler = match['battle']['starPlayer']['brawler']['name']
        else:
            while brawler == "":
                for team in match['battle']['teams']:
                    for player in team:
                        if player["tag"] == MAL_PLAIN:
                            brawler = player['brawler']['name']
    print(timestamp, " : ",game_mode, " : ",result, " : ",star_player, " : ",brawler)



#battleLogs.to_json('./temp.json')