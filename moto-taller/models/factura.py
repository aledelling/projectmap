from datetime import datetime
from database.db_config import db

class Factura(db.Model):
    __tablename__ = 'facturas'

    id = db.Column(db.Integer, primary_key=True)
    orden_id = db.Column(db.Integer, db.ForeignKey('ordenes_trabajo.id'), nullable=False)
    fecha_emision = db.Column(db.Date, nullable=False, default=datetime.utcnow)  # Using Date instead of DateTime
    subtotal = db.Column(db.Numeric(12, 2), nullable=False)  # For proper monetary values
    iva = db.Column(db.Numeric(12, 2), nullable=False)
    total = db.Column(db.Numeric(12, 2), nullable=False)

    # Relationship with order
    orden = db.relationship('OrdenTrabajo', backref='facturas')

    def __init__(self, orden_id, subtotal):
        self.orden_id = orden_id
        self.subtotal = subtotal
        self.calcular_impuestos()

    def calcular_impuestos(self):
        """Calculate IVA and total based on subtotal"""
        self.iva = round(float(self.subtotal) * 0.19, 2)
        self.total = round(float(self.subtotal) + float(self.iva), 2)

    def to_dict(self):
        return {
            'id': self.id,
            'orden_id': self.orden_id,
            'fecha_emision': self.fecha_emision.strftime('%Y-%m-%d'),
            'subtotal': float(self.subtotal),
            'iva': float(self.iva),
            'total': float(self.total)
        }

    def __repr__(self):
        return f'<Factura {self.id} - Orden {self.orden_id}>'