from flask import Flask, redirect, render_template, render_template, request, url_for, session
from flask_migrate import Migrate
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import os
from Models import *
from flask_wtf.csrf import CSRFProtect
from database import db
from consultas import *
from sqlalchemy import text

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'gafetes.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #   Trackear las modificaciones realizadas

app.config['SECRET_KEY'] = "MBDTF_21THCSM"

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


db.init_app(app)
migrate = Migrate()
migrate.init_app(app, db)
csrf = CSRFProtect(app)


@app.route('/', methods=["GET", "POST"])
def index():
    prestamos = text(inicio)
    query = db.session.execute(prestamos).fetchall()

    for gafete in query:
        print(gafete)

    return render_template("inicio.html") 

@app.route("/prueba", methods=["GET", "POST"])
def prueba():
    return render_template("prestamo.html")


@app.route("/prestamos", methods=["GET", "POST"])
def prestamo():
    return render_template("prestamo.html")

if __name__ == '__main__':
    app.run()
