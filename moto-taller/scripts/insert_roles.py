from app import create_app
from database.db_config import db
from models.rol_model import Rol

app = create_app()

with app.app_context():
    roles = ['administrador', 'tecnico', 'asesor', 'cliente']
    for nombre in roles:
        if not Rol.query.filter_by(nombre=nombre).first():
            db.session.add(Rol(nombre=nombre))
    db.session.commit()
    print("Roles insertados correctamente.")
