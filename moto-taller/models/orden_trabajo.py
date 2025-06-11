# models/orden_trabajo.py

from sqlalchemy.orm import relationship
from database import Base

class OrdenTrabajo(Base):
    __tablename__ = 'ordenes_trabajo'

    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    moto_id = Column(Integer, ForeignKey('motos.id'))
    tecnico_id = Column(Integer, ForeignKey('tecnicos.id'))
    descripcion = Column(String)
    estado = Column(String)
    fecha_entrada = Column(Date)
    fecha_salida = Column(Date)

    cliente = relationship('Cliente')
    moto = relationship('Moto')
    tecnico = relationship('Tecnico')
