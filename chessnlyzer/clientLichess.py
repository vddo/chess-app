"""Use Berserk framework to create a lichess API client. Fetch data and return to the app."""

import berserk
from flask import current_app, g
import os

# from chessnlyzer.db import get_db


def init_app(app):
    pass


def print_db_type():
    TOKEN_PATH = os.path.join(current_app.instance_path, 'lichess.api')
    print(current_app.instance_path)
    with open(TOKEN_PATH) as f:
        LICHESS_TOKEN = f.read().split('\n')[0]

    print(LICHESS_TOKEN)

    session = berserk.TokenSession(LICHESS_TOKEN)
    client = berserk.Client(session=session)

    userdata = client.account.get()
    username = userdata['username']
    blitz = userdata['perfs']['blitz']['rating']
    rapid = userdata['perfs']['rapid']['rating']
    puzzle = userdata['perfs']['puzzle']['rating']

    print(username)


def get_lichess_account():
    TOKEN_PATH = os.path.join(current_app.instance_path, 'lichess.api')
    with open(TOKEN_PATH) as f:
        LICHESS_TOKEN = f.read().split('\n')[0]

    session = berserk.TokenSession(LICHESS_TOKEN)
    client = berserk.Client(session=session)

    userdata = client.account.get()
    userdata_d = {}
    userdata_d['username'] = userdata['username']
    userdata_d['blitz'] = userdata['perfs']['blitz']['rating']
    userdata_d['rapid'] = userdata['perfs']['rapid']['rating']
    userdata_d['puzzle'] = userdata['perfs']['puzzle']['rating']

    try:
        g.db.execute(
            'INSERT INTO user (username, blitz, rapid, puzzle)'
            ' VALUES (?, ?, ?, ?)',
            (userdata_d['username'], userdata_d['blitz'], userdata_d['rapid'], userdata_d['puzzle'])
        )
        g.db.commit()

    except g.db.IntegrityError:
        pass

