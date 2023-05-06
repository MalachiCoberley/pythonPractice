#ya boi plays too much brawlstars, so i'm going to practice with the API.

import json
#DB Connection
import sqlite3

import urllib3
from api_keys import TEST_API_TOKEN
from brawl_utils import calculate_showdown_result, get_brawler_and_power_advantage

con = sqlite3.connect("brawl.db")
cur = con.cursor()

MAL_URL = '%2328RP22UYC'
MAL_PLAIN = '#28RP22UYC'
MAL_NAME = 'SleezyP'
CAL_URL = '%2320CL0P8C0'
CAL_PLAIN = '#20CL0P8C0'
CAL_NAME = 'OreganoSpindle'

WEEKEND_GAME_MODES = ['bigGame', 'roboRumble', 'bossFight']
SHOWDOWN_GAME_MODES = ["duoShowdown", "soloShowdown"]

http = urllib3.PoolManager()
headers = {'Authorization': f'Bearer {TEST_API_TOKEN}'}

def request_brawl_matches(player_url_tag) -> json:
    url = f'https://api.brawlstars.com/v1/players/{player_url_tag}/battlelog'
    resp = http.request('GET', url, headers=headers)
    jason = json.loads(resp.data)
    return jason

def write_data_to_db(data_list) -> None:
    for data in data_list:
        try:
            cur.execute("INSERT INTO matches VALUES(?,?,?,?,?,?,?,?,?)", data)
            con.commit()
            print(f"match logged for {data[2]}")
        except:
            pass

def extract_match_data(jason, player_tag, player_name) -> list:
    extracted_data = []
    for match in jason['items']:
        timestamp = match['battleTime']
        game_mode = match['battle']['mode']
        result = ""
        star_player = False
        brawler = ""
        power_advantage = 0
        #Skip over the record if it's a weekend mode
        if game_mode in WEEKEND_GAME_MODES:
            pass
        #Otherwise extract game info and write the match to the DB
        else:
            if game_mode in SHOWDOWN_GAME_MODES:
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
                #sometimes there are no star players?
                if match['battle']['starPlayer'] == None:
                    pass
                elif match['battle']['starPlayer']['tag'] == player_tag:
                    star_player = True
                brawler, power_advantage = get_brawler_and_power_advantage(match['battle']['teams'], player_tag)
            #return data tuple for DB
            data = (timestamp,player_tag,player_name,brawler,game_mode,result,star_player, power_advantage, str(match))
            extracted_data.append(data)
    return extracted_data


write_data_to_db(extract_match_data(request_brawl_matches(CAL_URL),CAL_PLAIN,CAL_NAME))
write_data_to_db(extract_match_data(request_brawl_matches(MAL_URL),MAL_PLAIN,MAL_NAME))


con.close()