<<<<<<< HEAD
from flask import Blueprint, render_template, request, redirect, session, url_for
from models.usuario import Usuario
from models.rol import Rol

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        usuario = Usuario.autenticar(correo, contrasena)
        if usuario:
            session['usuario_id'] = usuario['id']
            session['rol_id'] = usuario['rol_id']
            session['nombre'] = usuario['nombre']
            return redirect(url_for('dashboard'))  # Reemplazar con la ruta principal
        else:
            return render_template('usuarios/login.html', error="Credenciales inválidas")
    return render_template('usuarios/login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

=======
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.user_model import Usuario
from database.db_config import db

# Crea el Blueprint de autenticación
auth = Blueprint('auth', __name__)

# -------------------------
# RUTA PARA INICIAR SESIÓN
# -------------------------
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']

        user = Usuario.query.filter_by(correo=correo).first()

        if user and user.check_password(contraseña):
            session['usuario_id'] = user.id
            session['rol'] = user.rol

            flash('Sesión iniciada correctamente.', 'success')

            if user.rol == 'administrador':
                return redirect(url_for('admin.dashboard'))
            elif user.rol == 'tecnico':
                return redirect(url_for('tecnico.dashboard'))
            elif user.rol == 'asesor':
                return redirect(url_for('asesor.dashboard'))
            elif user.rol == 'cliente':
                return redirect(url_for('cliente.dashboard'))
            else:
                flash('Rol no reconocido.', 'danger')
                return redirect(url_for('auth.login'))

        flash('Credenciales incorrectas.', 'danger')

    return render_template('login.html')

# --------------------------
# RUTA PARA REGISTRO USUARIOS
# --------------------------
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        confirmar = request.form['confirmar']

        if contraseña != confirmar:
            flash('Las contraseñas no coinciden.', 'danger')
            return redirect(url_for('auth.register'))

        existente = Usuario.query.filter_by(correo=correo).first()
        if existente:
            flash('El correo ya está registrado.', 'warning')
            return redirect(url_for('auth.register'))

        nuevo_usuario = Usuario(nombre=nombre, correo=correo, rol='cliente')
        nuevo_usuario.set_password(contraseña)

        db.session.add(nuevo_usuario)
        db.session.commit()

        flash('¡Usuario registrado con éxito!', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')
>>>>>>> 4374d722241536cfd941335f0cacfd185640ca79
