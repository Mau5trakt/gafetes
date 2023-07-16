from functools import wraps
from flask import redirect, session


def login_required(f):
    """
    Decorate routes to require login.
    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("code") is None:
            return redirect("/iniciar")
        return f(*args, **kwargs)
    return decorated_function