# scripts/roles_permisos.py

from flask import Flask
from config.config import Config  # Importa la configuración desde config/config.py
from database.db_config import db
from models.rol_model import Rol

# Lista de roles por defecto
roles_por_defecto = [
    'administrador',
    'tecnico',
    'asesor',
    'cliente'
]

# Crea la app y configura la base de datos
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app

# Función para insertar roles si no existen
def insertar_roles(app):
    with app.app_context():
        db.create_all()  # Crea las tablas si no existen
        for nombre_rol in roles_por_defecto:
            if not Rol.query.filter_by(nombre=nombre_rol).first():
                nuevo_rol = Rol(nombre=nombre_rol)
                db.session.add(nuevo_rol)
                print(f"Rol '{nombre_rol}' insertado.")
        db.session.commit()
        print("Todos los roles han sido insertados correctamente.")

# Ejecutar script
if __name__ == '__main__':
    app = create_app()
    insertar_roles(app)
