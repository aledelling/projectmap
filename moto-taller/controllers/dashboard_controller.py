from flask import Blueprint, render_template, session, redirect, url_for, flash
from models.cliente import Cliente
from models.orden_trabajo import OrdenTrabajo
from models.factura import Factura
from models.moto import Moto           # 👈 Importa el modelo Moto
from models.tecnico import Tecnico     # 👈 Importa el modelo Técnico

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
def admin_dashboard():
    if 'usuario_id' not in session:
        flash('Debes iniciar sesión para acceder al sistema.', 'warning')
        return redirect(url_for('auth.login'))

    rol = session.get('rol')
    if rol not in ['administrador', 'tecnico', 'asesor']:
        flash('No tienes permiso para acceder al panel administrativo.', 'danger')
        return redirect(url_for('auth.login'))

    clientes = Cliente.query.all()
    ordenes = OrdenTrabajo.query.all()
    facturas = Factura.query.all()
    motos = Moto.query.all()               # 👈 Carga las motos
    tecnicos = Tecnico.query.all()         # 👈 Carga los técnicos

    return render_template('dashboard.html',
                           rol=rol,
                           username=session.get('username'),
                           clientes=clientes,
                           ordenes=ordenes,
                           facturas=facturas,
                           motos=motos,
                           tecnicos=tecnicos)  # 👈 Pasa los datos al template
