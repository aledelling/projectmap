from database.db_config import db

class Rol(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)

    # No necesitas agregar relación explícita aquí gracias al backref definido en Usuario
    # usuarios = db.relationship('Usuario', backref='rol') ← ya se definió desde el otro lado

    def __repr__(self):
        return f'<Rol {self.nombre}>'
