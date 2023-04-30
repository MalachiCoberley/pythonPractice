#testing ground for querying the db
import sqlite3

import pandas as pd

con = sqlite3.connect("brawl.db")
cur = con.cursor()

#res = cur.execute('select player_name, count(*) from matches where brawler = "MANDY" AND result = "defeat" group by player_name')
#print(res.fetchall())

df = pd.read_sql_query('Select * from matches', con)


con.close()