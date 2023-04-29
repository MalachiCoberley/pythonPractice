#ya boi plays too much brawlstars, so i'm going to practice with the API.

import json
#DB Connection
import sqlite3

import urllib3
from api_keys import TEST_API_TOKEN
from brawl_utils import calculate_showdown_result, is_showdown

con = sqlite3.connect("brawl.db")
cur = con.cursor()

MAL_URL = '%2328RP22UYC'
MAL_PLAIN = '#28RP22UYC'
MAL_NAME = 'SleezyP'
CAL_URL = '%2320CL0P8C0'
CAL_PLAIN = '#20CL0P8C0'
CAL_NAME = 'OreganoSpindle'

http = urllib3.PoolManager()
headers = {'Authorization': f'Bearer {TEST_API_TOKEN}'}

def request_brawl_matches(player_url_tag):
    url = f'https://api.brawlstars.com/v1/players/{player_url_tag}/battlelog'
    resp = http.request('GET', url, headers=headers)
    jason = json.loads(resp.data)
    return jason

#iterate through each match to fetch needed info
#TODO: may need to account for other non-standard matches like weekend-only modes.
def write_json_to_db(jason, player_tag, player_name):
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
                    if player["tag"] == player_tag:
                                brawler = player['brawler']['name']
            else:
                while brawler == "":
                    for team in match['battle']['teams']:
                        for player in team:
                            if player["tag"] == player_tag:
                                brawler = player['brawler']['name']
        #For duels, I'm just grabbing the first brawler. The info for this mode kind of sucks.
        elif game_mode == "duels":
            result = match['battle']['result']
            for player in match['battle']['players']:
                    if player["tag"] == player_tag:
                                brawler = player['brawlers'][0]['name']
        else:
            result = match['battle']['result']
            if match['battle']['starPlayer'] == None:
                pass
            elif match['battle']['starPlayer']['tag'] == player_tag:
                star_player = True
            while brawler == "":
                for team in match['battle']['teams']:
                    for player in team:
                        if player["tag"] == player_tag:
                            brawler = player['brawler']['name']
        print(timestamp, " : ",game_mode, " : ",result, " : ",star_player, " : ",brawler)
        #write to Sqlite DB
        data = (timestamp,player_tag,player_name,brawler,game_mode,result,star_player)
        try:
            cur.execute("INSERT INTO matches VALUES(?,?,?,?,?,?,?)", data)
            con.commit()
            print("match logged")
        except:
            print("already written")
            pass


write_json_to_db(request_brawl_matches(CAL_URL),CAL_PLAIN,CAL_NAME)
write_json_to_db(request_brawl_matches(MAL_URL),MAL_PLAIN,MAL_NAME)


#battleLogs.to_json('./temp.json')