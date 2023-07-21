import pytz
import datetime
from functools import wraps
from flask import redirect, session


def login_required(f):
    """
    Decorate routes to require login.
    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/iniciar")
        return f(*args, **kwargs)
    return decorated_function


def timestamp():
    utc_minus_600 = pytz.timezone('Etc/GMT+6')
    now = datetime.datetime.now(utc_minus_600)
    return now.strftime('%Y-%m-%d %H:%M:%S')
