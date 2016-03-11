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
        try:
            db.execute("""INSERT INTO user (username, password, email) VALUES (?, ? ,?)""", [username, password, email])
            db.commit()
        except sqlite3.IntegrityError as error:
            print "insertion de {username} est impossible : raison {message}".format(username=username,
                                                                                     message=error.message)


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


class Post(object):
    @classmethod
    def insert(cls, username, titre, text):
        db = get_db()
        user = User.get_user(username)

        db.execute("""INSERT INTO post (user_id, titre, text) VALUES (?, ? ,?)""",
                   [user['id'], titre, text])
        db.commit()

    @classmethod
    def get_posts(cls, username):
        db = get_db()
        cur = db.execute("""SELECT p.id, p.titre, p.text FROM post p INNER JOIN user u ON u.id = p.user_id
        WHERE username=?""", [username])

        result = cur.fetchall()
        return [{'id':post[0], 'titre':post[1], 'text':post[2]} for post in result]

class Commentaire(object):
    @classmethod
    def insert(cls, post_id, user_id, titre, text):
        db = get_db()
        db.execute("""INSERT INTO commentaire (post_id, user_id, titre, text) VALUES (?, ?, ? ,?)""",
                   [post_id, user_id, titre, text])
        db.commit()

    @classmethod
    def get_commentaires(cls, post_id):
        db = get_db()
        cur = db.execute("""SELECT c.id, c.titre, c.text FROM commentaire c INNER JOIN post p ON p.id = c.post_id
        WHERE post_id=?""", [post_id])

        result = cur.fetchall()
        return [{'id':post[0], 'titre':post[1], 'text':post[2]} for post in result]

