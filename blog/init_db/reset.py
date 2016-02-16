# coding=utf-8
from subprocess import call
DB_NAME = 'blog.db'
try:
    call(['rm {}'.format(DB_NAME)], shell=True)
except OSError as e:
    pass

call(['sqlite3 {} < blog/init_db/init.sql'.format(DB_NAME)], shell=True)

# init(DB_NAME)
