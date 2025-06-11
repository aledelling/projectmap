from database.db_config import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    # otros campos...

    motos = relationship('Moto', back_populates='cliente')
    ordenes = relationship('OrdenTrabajo', back_populates='cliente')
