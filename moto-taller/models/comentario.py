from flask_sqlalchemy import SQLAlchemy
from app import db  # Asegúrate de que esté importado desde donde defines `db`

class Comentario(db.Model):
    __tablename__ = 'comentarios'
    id_comentario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.Text, nullable=False)
    Correo = db.Column(db.Text, nullable=False)
    Informacion = db.Column(db.Text, nullable=True)
    Satisfecho = db.Column(db.Text, nullable=True)
    Visuales = db.Column(db.Text, nullable=True)
    Compra = db.Column(db.Text, nullable=True)
    Recomendacion = db.Column(db.Text, nullable=True)
    Mejoras = db.Column(db.Text, nullable=True)

    def guardar_comentario(self, datos):
        nuevo_comentario = Comentario(**datos)
        db.session.add(nuevo_comentario)
        db.session.commit()

    def obtener_comentarios(self):
        return Comentario.query.all()
