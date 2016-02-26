# coding=utf-8
import sqlite3

from app.models import User, Post
from app.views import app
with app.app_context():
    User.insert('toot', 'toto', 'paul.guichon@iedparis8.net')
    User.get_user('toot')
    Post.insert('toot', 'mon premier post', """
    jljlkj jljl jlj lj lj ljl jlj lj
    jljlkj jljl jlj lj lj ljl jlj lj
    jljlkj jljl jlj lj lj ljl jlj lj
    jljlkj jljl jlj lj lj ljl jlj lj
    jljlkj jljl jlj lj lj ljl jlj lj
    jljlkj jljl jlj lj lj ljl jlj lj
    jljlkj jljl jlj lj lj ljl jlj lj
    """)

    for post in Post.get_posts('toot'):
        print post
