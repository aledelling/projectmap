# cliente.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cedula = db.Column(db.String(20), unique=True, nullable=False)
    celular = db.Column(db.String(20))
    correo = db.Column(db.String(100))
    motos = db.relationship('Moto', backref='cliente', lazy=True)
