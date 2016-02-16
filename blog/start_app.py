# coding=utf-8
from app.views import app
from flask import g
try:
    import local_setings
except ImportError:
    local_setings = {}

HOST = local_setings.get('HOST', '0.0.0.0')
PORT = local_setings.get('PORT', 8000)
DEBUG = local_setings.get('DEBUG', True)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'sqlite_db', None)
    if db is not None:
        db.close()
if __name__ == '__main__':
    app.run(host=HOST, debug=DEBUG, port=PORT)