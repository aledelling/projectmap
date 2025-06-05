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
            session['username'] = user.nombre

            # Verificamos que el rol esté correctamente definido
            if user.rol and user.rol.nombre:
                rol_nombre = user.rol.nombre.lower().strip()
                session['rol'] = rol_nombre

                flash('Sesión iniciada correctamente.', 'success')

                # Redirigir según el rol
                if rol_nombre in ['administrador', 'tecnico', 'asesor']:
                    return redirect(url_for('dashboard.admin_dashboard'))
                elif rol_nombre == 'cliente':
                    return redirect(url_for('cliente.dashboard'))
                else:
                    flash('Rol no reconocido.', 'danger')
                    return redirect(url_for('auth.login'))
            else:
                flash('Usuario sin rol asignado.', 'danger')
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

        from models.rol_model import Rol  # Importación para evitar ciclos
        rol_cliente = Rol.query.filter_by(nombre='cliente').first()

        if not rol_cliente:
            flash('Error interno: rol "cliente" no está configurado.', 'danger')
            return redirect(url_for('auth.register'))

        nuevo_usuario = Usuario(nombre=nombre, correo=correo, rol=rol_cliente)
        nuevo_usuario.set_password(contraseña)

        db.session.add(nuevo_usuario)
        db.session.commit()

        flash('¡Usuario registrado con éxito!', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')
