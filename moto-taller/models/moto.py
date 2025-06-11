from database.db_config import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Moto(db.Model):
    __tablename__ = 'motos'

    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    placa = Column(String, nullable=False, unique=True)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)

    # Relación inversa con Cliente
    cliente = relationship('Cliente', back_populates='motos')

    # Relación con OrdenTrabajo
    ordenes = relationship('OrdenTrabajo', back_populates='moto')
