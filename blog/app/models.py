# coding=utf-8
import sqlite3
from ..init_db.reset import DB_NAME
conn = sqlite3.connect('../../{}.db'.format(DB_NAME))

