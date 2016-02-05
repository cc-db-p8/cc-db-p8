# coding=utf-8
import random
import sqlite3


def get_entry(nb):
    nom = '{}{}'.format(random.choice(['GUICHON', 'PARENT', 'SUPERMAN', 'RAMBO']), nb)
    prenom = '{}{}'.format(random.choice(['PAUL', 'ALEXANDRE', 'MATHIAS', 'TRUC']),nb)
    email = '{}.{}{}@{}'.format(nom, prenom, nb, random.choice(['gmail.com', 'hotmail.com', 'univ-paris8.fr']))
    sexe = random.choice(['M', 'F'])
    return [nom, prenom, email, sexe]


def init_personne(cursor):
    query = [get_entry(nb) for nb in range(100)]
    cursor.executemany('INSERT INTO personne (nom, prenom, email, sexe) VALUES (?, ?, ?, ?)', query)


def init_type(cusor):
    cusor.execute('INSERT INTO type_adresse (id, label) VALUES (1, "PERSONNEL"), (2, "TRAVAIL")')


def get_commune(nb):
    cod_pos = random.randrange(10000, 99999)
    cod_com = random.randrange(10000, 99999)
    label = '{} {}'.format(random.choice(['ST DENIS', 'PARIS', 'LION', 'TOULOUSE']), nb)
    return [cod_com, cod_pos, label]


def init_commune(cursor):
    query = [get_commune(nb) for nb in range(100)]
    cursor.executemany('INSERT INTO commune (cod_com, cod_pos, label) VALUES (?, ?, ?)', query)


def get_adresse(personne_id, nb, communes):
    type_id = random.choice([1, 2])
    label = '{} {}'.format(nb, random.choice(['rue general toto',
                                              'rue de paris',
                                              'rue du chateau']))
    cod_pos, cod_com = random.choice(communes)
    return [type_id, personne_id, label, cod_pos, cod_com]


def init_adresse(cursor):
    cursor.execute('SELECT id FROM personne')
    personnes = cursor.fetchall()
    cursor.execute('SELECT cod_pos, cod_com FROM commune')
    communes = cursor.fetchall()
    for nb, personne in enumerate(personnes):
        cursor.execute('INSERT INTO adresse(type_id, personne_id, label, cod_pos, cod_com) VALUES (?, ?, ?, ?, ?)',
                       get_adresse(personne[0], nb, communes))


def init(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    init_personne(cursor)
    conn.commit()
    init_type(cursor)
    conn.commit()
    init_commune(cursor)
    conn.commit()
    init_adresse(cursor)
    conn.commit()

    conn.close()
