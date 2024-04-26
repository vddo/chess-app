from flask import (
        Blueprint, g, flash, render_tempate, request, url_for
    )
from werkzeug.exceptions import abort

from chessnlyzer.db import get_db


bp = Blueprint('blog', __name__)
