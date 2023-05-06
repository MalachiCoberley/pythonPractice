# This is going to be a real prototype-ish way of managing migrations.
# I'll """ string up """ commands that don't need to be run anymore.

import sqlite3

con = sqlite3.connect("brawl.db")
cur = con.cursor()

"""
cur.execute("CREATE TABLE matches(timestamp, player_tag,player_name,brawler,game_mode,result,star_player, UNIQUE(timestamp,player_tag));")

# enacted May-2-2023, records prior will have a zero power advantage regardless of actual stats.
cur.execute("ALTER TABLE matches ADD COLUMN power_advantage integer default 0")

# enacted May-5-2023, records prior will have no raw json
cur.execute("ALTER TABLE matches ADD COLUMN brawl_dump text")
"""


con.commit()
con.close()
