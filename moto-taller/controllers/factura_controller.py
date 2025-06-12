from flask import Blueprint, request, redirect, url_for, flash, current_app
from datetime import datetime
from database.db_config import db
from models.factura import Factura
from models.orden_trabajo import OrdenTrabajo
import os
from werkzeug.utils import secure_filename

factura_bp = Blueprint('factura', __name__, url_prefix='/facturas')

def init_factura_config(app):
    upload_folder = os.path.join(app.root_path, 'static', 'facturas')
    app.config['UPLOAD_FOLDER_FACTURAS'] = upload_folder
    os.makedirs(upload_folder, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf'}

def crear_factura_db(orden_id, subtotal):
    try:
        iva = round(subtotal * 0.19, 2)
        total = round(subtotal + iva, 2)
        
        factura = Factura(
            orden_id=orden_id,
            fecha_emision=datetime.now(),
            subtotal=subtotal,
            iva=iva,
            total=total,
            pdf_path=None
        )
        
        db.session.add(factura)
        db.session.commit()
        return factura
    except Exception as e:
        db.session.rollback()
        raise e

@factura_bp.route('/generar_desde_dashboard', methods=['GET', 'POST'])
def generar_desde_dashboard():
    # Obtener órdenes completadas y no facturadas
    ordenes_pendientes = OrdenTrabajo.query.filter(
        OrdenTrabajo.estado == 'Listo para entrega',
        ~exists().where(Factura.orden_id == OrdenTrabajo.id)
    ).all()
    
    if request.method == 'POST':
        try:
            orden_id = int(request.form['orden_id'])
            subtotal = float(request.form['subtotal'])
            
            # Verificar que la orden existe y está pendiente
            orden = OrdenTrabajo.query.filter_by(
                id=orden_id,
                estado='Listo para entrega'
            ).first_or_404()
            
            # Crear la factura
            factura = crear_factura_db(orden_id, subtotal)
            
            # Actualizar estado de la orden
            orden.estado = 'facturada'
            db.session.commit()
            
            flash(f"Factura FAC-{factura.id} generada exitosamente", "success")
            return redirect(url_for('dashboard.admin_dashboard', _anchor='factura-section'))
            
        except ValueError:
            flash("Error: Datos inválidos en el formulario", "danger")
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Error al crear factura: {str(e)}")
            flash("Error al generar la factura", "danger")
    
    # Pasar las órdenes pendientes al template
    return render_template('tu_template.html', 
                         ordenes_pendientes=ordenes_pendientes,
                         show_form=True)

@factura_bp.route('/<int:id>')
def ver_factura(id):
    factura = Factura.query.get_or_404(id)
    return render_template('factura/detalle.html', factura=factura)

@factura_bp.route('/<int:id>/descargar')
def descargar_factura(id):
    factura = Factura.query.get_or_404(id)
    if not factura.pdf_path:
        flash("Esta factura no tiene un PDF asociado", "warning")
        return redirect(url_for('factura.ver_factura', id=id))
    
    upload_folder = current_app.config['UPLOAD_FOLDER_FACTURAS']
    return send_from_directory(
        upload_folder,
        factura.pdf_path,
        as_attachment=True,
        download_name=f'factura_{id}.pdf'
    )