# coding=utf-8
import sqlite3

from app.models import insert_user, select_user
from app.views import app
with app.app_context():
    insert_user('toot', 'toto', 'paul.guichon@iedparis8.net')
    select_user('toot')