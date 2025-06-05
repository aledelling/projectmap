from database.db_config import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    contraseña_hash = db.Column(db.String(128), nullable=False)

    # Relación con la tabla roles (clave foránea)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    rol = relationship("Rol", backref="usuarios")  # Objeto Rol relacionado

    def set_password(self, contraseña):
        """Genera un hash seguro para la contraseña del usuario"""
        self.contraseña_hash = generate_password_hash(contraseña)

    def check_password(self, contraseña):
        """Verifica si la contraseña ingresada coincide con el hash"""
        return check_password_hash(self.contraseña_hash, contraseña)

    def __repr__(self):
        return f'<Usuario {self.nombre} - {self.correo}>'
