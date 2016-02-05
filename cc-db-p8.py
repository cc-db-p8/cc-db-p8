# coding=utf-8

import sqlite3
conn = sqlite3.connect('exemple.db')

c = conn.cursor()

c.execute("SELECT * FROM personne")

print c.fetchall()

query = [["GUICHON{}".format(x), "PAUL{}".format(x)] for x in range(20)]


print query
c.executemany('INSERT INTO personne (nom, prenom) VALUES (?, ?)', query)
conn.commit()
#
# c.execute("SELECT * FROM personne")
#
# print c.fetchall()
#
# conn.close()
