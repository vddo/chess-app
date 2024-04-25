import click
from flask import current_app, g
import sqlite3

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None) 
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        f.read().decode('utf8')
