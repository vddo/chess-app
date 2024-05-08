from flask import (
        Blueprint, g, flash, render_template, request, url_for
    )

import chessnlyzer.clientLichess
from chessnlyzer.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    chessnlyzer.clientLichess.get_lichess_account()
    sel_res= db.execute('SELECT * FROM user WHERE id=1')
    userdata = sel_res.fetchone()

    return render_template('blog/index.html', userdata=userdata)
