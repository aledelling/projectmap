# controllers/orden_controller.py
from flask import Blueprint, render_template, session
from database import SessionLocal
from models.orden_trabajo import OrdenTrabajo

orden_bp = Blueprint('orden', __name__)
db = SessionLocal()

@orden_bp.route('/dashboard')
def dashboard():
    if 'rol' not in session:
        return redirect('/login')  # Redirige si no hay sesión

    ordenes = db.query(OrdenTrabajo).all()
    return render_template('dashboard.html', ordenes=ordenes)
