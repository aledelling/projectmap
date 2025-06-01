# Importa las funciones necesarias de Flask
from flask import Blueprint, render_template, request, redirect, url_for, session, flash

# Importa la clase Usuario correctamente con mayúscula desde el modelo usuario.py
from models.user_model import Usuario

# Importa la sesión de base de datos (si estás usando SQLAlchemy)
from database.db_config import db

# Crea un Blueprint llamado 'auth' que maneja rutas relacionadas con autenticación
auth_bp = Blueprint('auth', __name__)

# Define la ruta para login, aceptando métodos GET y POST
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Si el formulario fue enviado (POST)
    if request.method == 'POST':
        # Obtiene el correo y la contraseña ingresados en el formulario
        correo = request.form['correo']
        contraseña = request.form['contraseña']

        # Busca un usuario con ese correo en la base de datos
        user = Usuario.query.filter_by(correo=correo).first()

        # Verifica si el usuario existe y si la contraseña es correcta
        if user and user.check_password(contraseña):
            # Si es válido, guarda su ID y rol en la sesión
            session['usuario_id'] = user.id
            session['rol'] = user.rol

            # Redirige al usuario a su dashboard según su rol
            if user.rol == 'administrador':
                return redirect(url_for('admin.dashboard'))
            elif user.rol == 'tecnico':
                return redirect(url_for('tecnico.dashboard'))
            elif user.rol == 'asesor':
                return redirect(url_for('asesor.dashboard'))
            elif user.rol == 'cliente':
                return redirect(url_for('cliente.dashboard'))

        else:
            # Si las credenciales son incorrectas, muestra un mensaje de error
            flash('Credenciales incorrectas.')

    # Si es GET o hay error, muestra el formulario de login
    return render_template('login.html')
