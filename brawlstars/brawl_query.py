#testing ground for querying the db
import sqlite3

import pandas as pd

con = sqlite3.connect("brawl.db")
cur = con.cursor()

df = pd.read_sql_query('Select * from matches', con)

print(df)

con.close()