# coding=utf-8
from __future__ import absolute_import
import sqlite3
from flask import g


def connect_db():
    return sqlite3.connect('blog.db')


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


class User(object):
    """
    Class permettant de manipuler la table User
    """
    @classmethod
    def insert(cls, username, password, email):
        db = get_db()
        db.execute("""INSERT INTO user (username, password, email) VALUES (?, ? ,?)""", [username, password, email])
        db.commit()

    @classmethod
    def inserts(cls, users):
        """
        :param users:
        :type users: tableau d'user [[username, password, email]]
        :return:
        :rtype:
        """
        db = get_db()
        db.execute("""INSERT INTO user (username, password, email) VALUES (?, ? ,?)""", users)
        db.commit()

    @classmethod
    def get_user(cls, username):
        db = get_db()
        cur = db.execute("""SELECT id, username, email FROM user WHERE username=?""", [username])
        result = cur.fetchone()
        if result:
            result = {
                'id': result[0],
                'username': result[1],
                'email': result[2]
            }
        return result