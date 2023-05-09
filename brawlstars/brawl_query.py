#testing ground for querying the db
import sqlite3

import numpy as np
import pandas as pd

from brawl_utils import convert_utc_to_az_datetime

con = sqlite3.connect("brawl.db")
cur = con.cursor()

### Bar Graph of Relative Win/Loss With Each Brawler ###
matches = pd.read_sql_query('Select player_name Player, brawler Brawler, CASE result WHEN "victory" THEN 1 ELSE -1 END as Result from matches', con)
brawler_stats_by_player = pd.crosstab(values=matches['Result'], index=matches['Brawler'], columns=matches['Player'], aggfunc=np.sum)
#Replace NaN with zero after setting the zero values to .01 to distinguish a "zero" from "no data"
brawler_stats_by_player = brawler_stats_by_player.replace(0,.01).fillna(0)
brawler_stats_by_player.plot.barh(figsize=(20, 15), width=0.8)



### Show Top 3 Brawlers Per Player ###
# This version of sqlite doesn't seem to like window functions, so i'm just doing two separate queries
#this also fucking sucks. so I need to revisit it.
mal_top_brawlers = pd.read_sql_query('Select player_name, brawler, count(brawler) as matches_played from matches where player_name = "SleezyP" group by player_name, brawler order by matches_played desc Limit 3', con)
cal_top_brawlers = pd.read_sql_query('Select player_name, brawler, count(brawler) as matches_played from matches where player_name = "OreganoSpindle" group by player_name, brawler order by matches_played desc Limit 3', con)
top_brawlers = [mal_top_brawlers, cal_top_brawlers]
for df in top_brawlers:
    print(df)

"""
def performance_over_time(con):
    #player_name = input('What is your player name?')
    #brawler = input('What brawler do you want to view?').upper()
    player_name = 'SleezyP'
    brawler = 'ASH'

    results = pd.read_sql_query('Select * from matches where player_name = ? and brawler = ?', con, params=(player_name, brawler))
    
    for idx, row in results.iterrows():
        print(convert_utc_to_az_datetime(row['timestamp']))

performance_over_time(con)
"""

con.close()