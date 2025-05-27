#cliente_controller.py
# Importa las herramientas necesarias de Flask:
# Blueprint: para organizar rutas por módulos
# render_template: para renderizar archivos HTML
# request: para acceder a los datos enviados en formularios
# redirect y url_for: para redirigir a otras rutas
from flask import Blueprint, render_template, request, redirect, url_for

# Importa el modelo Cliente y la instancia de la base de datos db
from models.cliente import Cliente, db

# Crea un Blueprint llamado 'cliente_bp' para agrupar las rutas relacionadas con clientes
cliente_bp = Blueprint('cliente_bp', __name__)

# Ruta para listar todos los clientes
@cliente_bp.route('/clientes')
def listar_clientes():
    # Consulta todos los registros de la tabla Cliente
    clientes = Cliente.query.all()

    # Renderiza la plantilla HTML 'cliente/listar.html' y le pasa la lista de clientes
    return render_template('cliente/listar.html', clientes=clientes)

# Ruta para crear un nuevo cliente (soporta métodos GET y POST)
@cliente_bp.route('/clientes/nuevo', methods=['GET', 'POST'])
def nuevo_cliente():
    # Si se envió el formulario (POST), se procesan los datos
    if request.method == 'POST':
        # Obtiene los valores del formulario HTML
        nombre = request.form['nombre']
        cedula = request.form['cedula']
        celular = request.form['celular']
        correo = request.form['correo']

        # Crea un nuevo objeto Cliente con los datos recibidos
        nuevo = Cliente(nombre=nombre, cedula=cedula, celular=celular, correo=correo)

        # Agrega el nuevo cliente a la sesión de la base de datos
        db.session.add(nuevo)

        # Guarda los cambios en la base de datos
        db.session.commit()

        # Redirige a la ruta que lista los clientes
        return redirect(url_for('cliente_bp.listar_clientes'))

    # Si el método es GET, muestra el formulario para crear un nuevo cliente
    return render_template('cliente/nuevo.html')
