from database.db_config import db
from models.user_model import Usuario  # Asegúrate de importar todos los modelos que necesites

def init_db():
    db.create_all()

