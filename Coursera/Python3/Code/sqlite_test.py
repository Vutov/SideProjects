import sqlite3

con = sqlite3.connect('population.db')
cur = con.cursor()

cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)')
cur.execute('INSERT INTO PopByRegion VALUES("Central Africa", 330993)')
cur.execute('INSERT INTO PopByRegion VALUES("Southeastern Africa", 743112)')
cur.execute('INSERT INTO PopByRegion VALUES("Japan", 100562)')

cur.execute('SELECT Region, Population FROM PopByRegion WHERE Population > 110000 ORDER BY Region ASC')

cur.fetchone()
cur.fetchall()

con.commit()
