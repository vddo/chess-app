"""Use Berserk framework to create a lichess API client. Fetch data and return to the app."""

import berserk
from flask import current_app, g
import os

# from chessnlyzer.db import get_db

def init_app(app):
    pass


def print_db_type():
    print(current_app.instance_path)
    api_path = os.path.join(current_app.instance_path, 'lichess.api')
    with open(api_path) as f:
        LICHESS_TOKEN = f.read().split('\n')[0]

    print(LICHESS_TOKEN)

    session = berserk.TokenSession(LICHESS_TOKEN)
    client = berserk.Client(session=session)

    userdata = client.account.get()
    username = userdata['username']
    blitz = userdata['perfs']['blitz']['rating']
    rapid = userdata['perfs']['rapid']['rating']
    puzzle = userdata['perfs']['puzzle']['rating']


def get_lichess_account():
    pass
