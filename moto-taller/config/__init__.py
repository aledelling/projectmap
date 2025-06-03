import os

class Config:
    # Ruta absoluta a la base de datos dentro de la carpeta database
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, '..', 'database', 'moto_taller.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'clave-secreta-123'
