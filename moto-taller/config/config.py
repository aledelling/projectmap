# config/config.py

import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # /config
    PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))  # /moto-taller
    DATABASE_PATH = os.path.join(PROJECT_DIR, 'database', 'moto_taller.db')

    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'supersecreto'  # Puedes cambiarlo
