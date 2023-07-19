from database import db
from functions import timestamp

class Usuarios(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    usuario = db.Column(db.String(20), nullable=False)
    hash = db.Column(db.String(200), nullable=False)

    prestamos = db.relationship('Prestamos', back_populates='usuarios')

class Gafetes(db.Model):
    id_gafete = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String(20), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    prestado = db.Column(db.String(1), nullable=False, default=0)

    prestamos = db.relationship('Prestamos', back_populates='gafetes')

class Prestamos(db.Model):
    id_prestamo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    gafete_id = db.Column(db.Integer, db.ForeignKey('gafetes.id_gafete'))
    nombre_prestamo = db.Column(db.String(100), nullable=False)
    cedula = db.Column(db.String(20))
    empresa = db.Column(db.String(100))
    autoriza = db.Column(db.String(100))
    hora_inicio = db.Column(db.String(100), default=timestamp())
    hora_fin = db.Column(db.String(100))

    usuarios = db.relationship('Usuarios', back_populates='prestamos')
    gafetes = db.relationship('Gafetes', back_populates='prestamos')

    #Crear la tabla con todos los campos a traves de una consulta
