# coding=utf-8
from subprocess import call
from populate import init
DB_NAME = 'exemple.db'
try:
    call(['rm {}'.format(DB_NAME)], shell=True)
except OSError as e:
    print(e.message)

call(['sqlite3 exemple.db < init_db/init.sql'], shell=True)

init(DB_NAME)
