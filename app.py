from flask import Flask, redirect, render_template, render_template, request, url_for, session, flash
from flask_migrate import Migrate
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import os
from Models import *
from flask_wtf.csrf import CSRFProtect
from database import db
from consultas import *
from sqlalchemy import text
from functions import *

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
Session(app)


@app.route('/', methods=["GET", "POST"])
def index():
    prestamos = text(inicio)
    query = db.session.execute(prestamos).fetchall()

    for gp in query:
        print(gp.nombre_prestamo, gp.cedula, gp.empresa, gp.tipo, gp.numero)

    try:
        loged = False
        user = ""
        if session["user_id"]:
            loged = True
            user = session["user"]

    except:
        loged = False

    print(loged)
    return render_template("inicio.html", loged=loged, user=user, prestamos=query)

@app.route('/iniciar', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if not request.form.get("usuario"):
            flash("No introdujo usuario")
        if not request.form.get("password"):
            flash("No introdujo contraseña")

        usuario = request.form.get("usuario")
        password = request.form.get("password")
        print('--------------')
        usuario = Usuarios.query.filter_by(usuario=usuario).first()
        if not usuario or not check_password_hash(usuario.hash, password):
            flash("Usuario o contraseña incorrecta")
        else:
            session["user_id"] = usuario.id_usuario
            session["user"] = usuario.usuario
            return redirect("/")

    return render_template("login.html")


@app.route("/prestamos", methods=["GET", "POST"])
@login_required
def prestamo():
    loged = True

    if request.method == "POST":
        if not request.form.get("nombre"):
            flash("No introdujo nombre")
        if not request.form.get("ngafete"):
            flash("Introduzca un numero de gafete")

        nombre = request.form.get("nombre")

        tipo = request.form.get("tipo")
        cedula = request.form.get("cedula")
        empresa = request.form.get("empresa")
        autoriza = request.form.get("autoriza")
        ngafete = request.form.get("ngafete")


        gafete_modificar = Gafetes.query.filter_by(tipo=tipo, numero=ngafete).first()
        if not gafete_modificar:
            flash("Numero de gafete Invalido")
        elif gafete_modificar.prestado == "1":
            flash("Gafete ya prestado")

        else:
            insercion = Prestamos(
            usuario_id = 1,
            gafete_id = ngafete,
            nombre_prestamo = nombre,
            cedula = cedula,
            empresa = empresa,
            autoriza = autoriza,
            hora_inicio = timestamp())

            gafete_modificar.prestado = "1"

            db.session.add(insercion)
            db.session.commit()


    return render_template("prestamo.html", user=session["user"], loged=loged)

@app.route("/devolucion/<int:id_prestamo>")
@login_required
def devolucion(id_prestamo):
    prestamo = Prestamos.query.filter_by(id_prestamo=id_prestamo).first()
    gafete = Gafetes.query.filter_by(id_gafete=prestamo.gafete_id).first()

    if prestamo and gafete:
        print("Hay ambos")
        prestamo.hora_fin = timestamp()
        gafete.prestado = "0"
        flash(f"Se ha devuelto el gafete '{gafete.tipo}: {gafete.numero}'  ")  # ex staff 5"""
        db.session.commit()



    return(redirect(url_for("index")))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()
