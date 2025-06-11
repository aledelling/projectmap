# models/tecnico.py

from database.db_config import db
from sqlalchemy import Column, Integer, String, Date

class Tecnico(db.Model):
    __tablename__ = 'tecnico'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    especialidad = Column(String, nullable=False)
    celular = Column(String, nullable=False)
    fecha_ingreso = Column(Date, nullable=False)
