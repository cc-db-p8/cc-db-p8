# coding=utf-8

import sqlite3
conn = sqlite3.connect('exemple.db')

cursor = conn.cursor()

cursor.execute("""SELECT p.nom, a.type_id, ta.label, a.label, a.cod_pos, a.cod_com FROM personne p, adresse a, type_adresse ta
WHERE p.id=a.personne_id and a.type_id=ta.id""")

for x in cursor.fetchall():
    print x

cursor.execute("""SELECT p.nom, a.type_id, ta.label, a.label, a.cod_pos, a.cod_com FROM personne p
    INNER JOIN  adresse a ON p.id=a.personne_id LEFT JOIN type_adresse ta ON a.type_id=ta.id""")

for x in cursor.fetchall():
    print x
