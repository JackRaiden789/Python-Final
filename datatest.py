import sqlite3

conn = sqlite3.connect('./grocery.sqlite')
cur = conn.cursor()

cur.execute('SELECT item, qty FROM Grocery')
for i in cur:
    print(i)