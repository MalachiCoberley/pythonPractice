#testing ground for querying the db
import sqlite3

import pandas as pd
import numpy as np

con = sqlite3.connect("brawl.db")
cur = con.cursor()

### Bar Graph of Relative Win/Loss With Each Brawler ###
matches = pd.read_sql_query('Select player_name Player, brawler Brawler, CASE result WHEN "victory" THEN 1 ELSE -1 END as Result from matches', con)
brawler_stats_by_player = pd.crosstab(values=matches['Result'], index=matches['Brawler'], columns=matches['Player'], aggfunc=np.sum)
#Replace NaN with zero after setting the zero values to .01 to distinguish a "zero" from "no data"
brawler_stats_by_player = brawler_stats_by_player.replace(0,.01).fillna(0)
brawler_stats_by_player.plot.bar()



con.close()