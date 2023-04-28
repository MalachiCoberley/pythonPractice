# This is going to be a real prototype-ish way of managing migrations.
# I'll """ string up """ commands that don't need to be run anymore.

import sqlite3
con = sqlite3.connect("brawl.db")
cur = con.cursor()

cur.execute("CREATE TABLE matches(timestamp, player_tag,player_name,brawler,game_mode,result,star_player, UNIQUE(timestamp,player_tag));")

