from flask import (
        Blueprint, g, flash, render_template, request, url_for
    )
from werkzeug.exceptions import abort

import chessnlyzer.clientLichess
from chessnlyzer.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    chessnlyzer.clientLichess.get_lichess_account()
    return render_template('blog/index.html')
