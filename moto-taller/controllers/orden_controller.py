from flask import Blueprint

orden_bp = Blueprint('orden_bp', __name__)

@orden_bp.route('/ejemplo')
def ejemplo():
    return "Ruta de ejemplo para órdenes"
