from database.db_config import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    cedula = Column(String, nullable=False, unique=True)
    celular = Column(String, nullable=False)
    correo = Column(String, nullable=True)

    motos = relationship('Moto', back_populates='cliente')
    ordenes = relationship('OrdenTrabajo', back_populates='cliente')
