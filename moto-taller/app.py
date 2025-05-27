# app.py

# Importa la clase Flask desde el módulo flask, que permite crear la aplicación web
from flask import Flask

# Importa los blueprints (controladores) que manejan las rutas relacionadas a clientes
from controllers.cliente_controller import cliente_bp

# Importa los blueprints que manejan las rutas relacionadas a órdenes
from controllers.orden_controller import orden_bp

# Importa los blueprints que manejan las rutas de autenticación (login, registro, etc.)
from controllers.auth_controller import auth_bp

# Importa las funciones para conectar y cerrar la base de datos
from database.init_db import get_db, close_db

# Define una función que crea y configura la aplicación Flask
def create_app():
    # Crea una instancia de la aplicación Flask
    app = Flask(__name__)

    # Carga la configuración desde el archivo 'config.py'
    app.config.from_object('config')

    # Registro de blueprints (controladores) con prefijos en la URL
    app.register_blueprint(cliente_bp, url_prefix='/clientes')  # Todas las rutas de cliente empiezan con /clientes
    app.register_blueprint(orden_bp, url_prefix='/ordenes')     # Todas las rutas de orden empiezan con /ordenes
    app.register_blueprint(auth_bp, url_prefix='/auth')         # Todas las rutas de auth empiezan con /auth

    # Antes de cada solicitud, se establece la conexión a la base de datos
    @app.before_request
    def before_request():
        get_db()  # Abre o recupera la conexión actual a la base de datos

    # Después de que termina el contexto de la aplicación (respuesta enviada), se cierra la conexión
    @app.teardown_appcontext
    def teardown(exception):
        close_db()  # Cierra la conexión con la base de datos

    # Ruta principal del sitio
    @app.route('/')
    def index():
        return "Bienvenido al sistema de Moto-Taller"  # Respuesta al acceder a la raíz del sitio

    # Devuelve la aplicación configurada
    return app

# Punto de entrada cuando se ejecuta el script directamente
if __name__ == '__main__':
    # Crea la aplicación Flask
    app = create_app()

    # Abre el contexto de la aplicación para ejecutar operaciones como la inicialización de la base de datos
    with app.app_context():
        from database.init_db import init_db
        init_db()  # Inicializa la base de datos (crea las tablas si no existen)

    # Ejecuta la aplicación en modo depuración (debug), útil para desarrollo
    app.run(debug=True)
