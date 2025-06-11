from flask import Blueprint, render_template, request, redirect, url_for, session
from database.db_config import db
from models.orden_trabajo import OrdenTrabajo
from models.cliente import Cliente
from models.moto import Moto
from models.tecnico import Tecnico
from datetime import datetime

orden_bp = Blueprint('orden', __name__)

@orden_bp.route('/ordenes')
def ver_ordenes():
    if 'rol' not in session:
        return redirect('/auth/login')

    ordenes = OrdenTrabajo.query.all()
    return render_template('dashboard.html', ordenes=ordenes)

@orden_bp.route('/ordenes/nueva', methods=['GET', 'POST'])
def nueva_orden():
    if 'rol' not in session:
        return redirect('/auth/login')

    if request.method == 'POST':
        nueva = OrdenTrabajo(
            cliente_id=request.form['cliente_id'],
            moto_id=request.form['moto_id'],
            tecnico_id=request.form['tecnico_id'],
            descripcion=request.form['descripcion'],
            fecha_entrada=datetime.strptime(request.form['fecha_entrada'], '%Y-%m-%d'),
            estado='Pendiente'
        )
        db.session.add(nueva)
        db.session.commit()
        return redirect(url_for('orden.ver_ordenes'))

    clientes = Cliente.query.all()
    motos = Moto.query.all()
    tecnicos = Tecnico.query.all()
    return render_template('nueva_orden.html', clientes=clientes, motos=motos, tecnicos=tecnicos)
