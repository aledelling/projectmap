from flask import Blueprint, render_template, request, send_file
from models.factura import Factura
from datetime import datetime
from io import BytesIO
from reportlab.pdfgen import canvas

factura_bp = Blueprint('factura', __name__)
factura_model = Factura()

@factura_bp.route('/facturar', methods=['GET', 'POST'])
def generar_factura():
    if request.method == 'POST':
        orden_id = request.form['orden_id']
        subtotal = float(request.form['subtotal'])
        iva = subtotal * 0.19
        total = subtotal + iva
        fecha_emision = datetime.now().strftime('%Y-%m-%d')

        factura_id = factura_model.crear_factura(orden_id, fecha_emision, subtotal, iva, total)

        # Generar PDF
        datos = factura_model.obtener_datos_factura(factura_id)
        buffer = BytesIO()
        p = canvas.Canvas(buffer)
        p.drawString(100, 800, f"Factura ID: {datos['id']}")
        p.drawString(100, 780, f"Cliente: {datos['cliente']}")
        p.drawString(100, 760, f"Placa Moto: {datos['placa']}")
        p.drawString(100, 740, f"Descripción: {datos['descripcion']}")
        p.drawString(100, 720, f"Fecha de Emisión: {datos['fecha_emision']}")
        p.drawString(100, 700, f"Subtotal: {datos['subtotal']}")
        p.drawString(100, 680, f"IVA: {datos['iva']}")
        p.drawString(100, 660, f"Total: {datos['total']}")
        p.showPage()
        p.save()

        buffer.seek(0)
        return send_file(buffer, as_attachment=False, download_name='factura.pdf', mimetype='application/pdf')

    ordenes = factura_model.obtener_ordenes_pendientes()
    return render_template('factura.html', ordenes=ordenes)


