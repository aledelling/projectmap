from flask import Blueprint, render_template, session, redirect, url_for, flash

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
def admin_dashboard():
    # Validar si el usuario está en sesión
    if 'usuario_id' not in session:
        flash('Debes iniciar sesión para acceder al sistema.', 'warning')
        return redirect(url_for('auth.login'))

    # Validar si el rol tiene acceso al panel administrativo
    rol = session.get('rol')
    if rol not in ['administrador', 'tecnico', 'asesor']:
        flash('No tienes permiso para acceder al panel administrativo.', 'danger')
        return redirect(url_for('auth.login'))

    # Renderizar el dashboard administrativo
    return render_template('dashboard.html', rol=rol, username=session.get('username'))
