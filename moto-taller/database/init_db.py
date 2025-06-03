from database.db_config import db
from models.user_model import Usuario
from models.rol_model import Rol

def init_db():
    db.create_all()
