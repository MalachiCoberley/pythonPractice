#testing ground for querying the db
import sqlite3

con = sqlite3.connect("brawl.db")
cur = con.cursor()

res = cur.execute("Select * from matches")
print(res.fetchall())