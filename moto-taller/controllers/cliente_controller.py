from flask import Blueprint, render_template, request, redirect, url_for
from models.cliente import Cliente, db

cliente_bp = Blueprint('cliente_bp', __name__)

@cliente_bp.route('/clientes/nuevo', methods=['GET', 'POST'])
def nuevo_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cedula = request.form['cedula']
        celular = request.form['celular']
        correo = request.form['correo']

        nuevo = Cliente(nombre=nombre, cedula=cedula, celular=celular, correo=correo)
        db.session.add(nuevo)
        db.session.commit()

        return redirect(url_for('dashboard.admin_dashboard'))  # <- Redirige al dashboard

    return render_template('clientes/nuevo.html')
