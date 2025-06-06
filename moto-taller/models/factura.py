from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()  # Asegúrate de que 'db' esté disponible aquí o usa una inicialización diferida

class Factura(db.Model):
    __tablename__ = 'facturas'
    id = db.Column(db.Integer, primary_key=True)
    orden_id = db.Column(db.Integer, nullable=False)
    fecha_emision = db.Column(db.String, nullable=False)
    subtotal = db.Column(db.Float, nullable=False)
    iva = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)

    def crear_factura(self, orden_id, fecha_emision, subtotal, iva, total):
        nueva_factura = Factura(
            orden_id=orden_id,
            fecha_emision=fecha_emision,
            subtotal=subtotal,
            iva=iva,
            total=total
        )
        db.session.add(nueva_factura)
        db.session.commit()
        return nueva_factura.id

    def obtener_datos_factura(self, factura_id):
        factura = Factura.query.get(factura_id)
        # Aquí simula datos adicionales
        return {
            'id': factura.id,
            'cliente': 'Juan Pérez',
            'placa': 'ABC123',
            'descripcion': 'Servicio general',
            'fecha_emision': factura.fecha_emision,
            'subtotal': factura.subtotal,
            'iva': factura.iva,
            'total': factura.total
        }

    def obtener_ordenes_pendientes(self):
        # Simulación. En la práctica deberías consultar otra tabla
        return [{'id': 1, 'descripcion': 'Cambio de aceite'}, {'id': 2, 'descripcion': 'Revisión'}]
