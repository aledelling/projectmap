# app.py

from flask import Flask, render_template  # Importa render_template para usar HTML

# Importa los blueprints (controladores)
from controllers.cliente_controller import cliente_bp
from controllers.orden_controller import orden_bp
from controllers.auth_controller import auth_bp

# Importa la instancia de SQLAlchemy desde db_config
from database.db_config import db

# Importa la clase de configuración
from config import Config

# Función para crear y configurar la aplicación Flask
def create_app():
    app = Flask(__name__)

    # Carga la configuración desde la clase Config
    app.config.from_object(Config)

    # Inicializa SQLAlchemy con la app
    db.init_app(app)

    # Registro de Blueprints con prefijos
    app.register_blueprint(cliente_bp, url_prefix='/clientes')
    app.register_blueprint(orden_bp, url_prefix='/ordenes')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Ruta raíz que renderiza una plantilla HTML
    @app.route('/')
    def index():
        return render_template('index.html')  # Muestra página HTML

    return app

# Punto de entrada principal
if __name__ == '__main__':
    app = create_app()

    # Inicializa la base de datos dentro del contexto de la app
    with app.app_context():
        from database.init_db import init_db
        init_db()

    # Ejecuta la aplicación en modo desarrollo
    app.run(debug=True)
