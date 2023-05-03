from dateutil import parser
from datetime import timedelta, datetime

def calculate_showdown_result(mode, rank):
    if mode == "duoShowdown":
        if rank < 3:
            return "victory"
        else:
            return "defeat"
    else:
        if rank < 5:
            return "victory"
        else:
            return "defeat"

def get_brawler_and_power_advantage(teams, player_tag) -> tuple:
    # return a specific player's brawler and the difference between your team's total power and the enemy's
    # negative number represents a disadvantage
    player_brawler = ""
    power_difference = 0
    for team in teams:
        total_team_power = 0
        is_enemy_team = True
        for player in team:
            if player['tag'] == player_tag:
                player_brawler = player['brawler']['name'] 
                is_enemy_team = False
            total_team_power += int(player['brawler']['power'])
        if is_enemy_team:
            total_team_power *= -1
        power_difference += total_team_power
    return (player_brawler, power_difference)

def convert_utc_to_az_datetime(date_str) -> datetime:
    date = parser.parse(date_str)
    az_timezone_adjustment = timedelta(hours=7)
    date -= az_timezone_adjustment
    print(type(date))
    return date