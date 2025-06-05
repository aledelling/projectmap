from flask import Blueprint, render_template, request, redirect, url_for
from models.usuario import Usuario
from models.rol import Rol

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios')
def lista_usuarios():
    usuarios = Usuario.obtener_todos()
    return render_template('usuarios/lista_usuarios.html', usuarios=usuarios)

@usuarios_bp.route('/usuarios/crear', methods=['GET', 'POST'])
def crear_usuario():
    roles = Rol.obtener_todos()
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        rol_id = request.form['rol_id']
        Usuario.crear(nombre, correo, contrasena, rol_id)
        return redirect(url_for('usuarios.lista_usuarios'))
    return render_template('usuarios/crear_usuario.html', roles=roles)

