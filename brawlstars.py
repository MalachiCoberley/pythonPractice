#ya boi plays too much brawlstars, so i'm going to practice with the API.

import urllib3
import pandas
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
for match in jason['items']:
    timestamp = match['battleTime']
    game_mode = match['battle']['mode']
    result = ""
    star_player = False
    brawler = ""
    if is_showdown(game_mode):
        result = calculate_showdown_result(game_mode, match['battle']['rank'])
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



#Timestamp - items[idx].battleTime
#playerTag - <passed in>
#playerName - <passed in>
#brawler - items[idx].battle.teams[idx].tag == <passed in tag>.brawler.name
#gameMode - items[idx].battle.mode
#result - items[idx].battle.result
#starPlayer - items[idx].battle.starPlayer.tag == <passed in tag>


#battleLogs.to_json('./temp.json')