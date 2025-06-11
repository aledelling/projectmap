from database.db_config import db
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class OrdenTrabajo(db.Model):
    __tablename__ = 'ordenes_trabajo'

    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    moto_id = Column(Integer, ForeignKey('motos.id'), nullable=False)
    tecnico_id = Column(Integer, ForeignKey('tecnico.id'), nullable=False)
    descripcion = Column(String, nullable=False)
    fecha_entrada = Column(Date, nullable=False)
    estado = Column(String, nullable=False)

    cliente = relationship('Cliente', back_populates='ordenes')
    moto = relationship('Moto', back_populates='ordenes')
    tecnico = relationship('Tecnico')
