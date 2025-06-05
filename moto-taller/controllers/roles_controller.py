from flask import Blueprint, render_template, request, redirect, url_for
from models.rol import Rol

roles_bp = Blueprint('roles', __name__)

@roles_bp.route('/roles')
def lista_roles():
    roles = Rol.obtener_todos()
    return render_template('roles/lista_roles.html', roles=roles)

@roles_bp.route('/roles/crear', methods=['GET', 'POST'])
def crear_rol():
    if request.method == 'POST':
        nombre = request.form['nombre']
        Rol.crear(nombre)
        return redirect(url_for('roles.lista_roles'))
    return render_template('roles/crear_rol.html')

