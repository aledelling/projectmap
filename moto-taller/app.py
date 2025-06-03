# app.py

from flask import Flask, render_template

# Importa los blueprints (controladores)
from controllers.cliente_controller import cliente_bp
from controllers.orden_controller import orden_bp
from controllers.auth_controller import auth  # ← Cambiado a "auth"

# Importa la instancia de SQLAlchemy
from database.db_config import db

# Importa la clase de configuración
from config.config import Config

# Función para crear y configurar la aplicación Flask
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    print("Conectando a la base de datos:", app.config['SQLALCHEMY_DATABASE_URI'])

    # Inicializa SQLAlchemy con la app
    db.init_app(app)

    # Registro de Blueprints
    app.register_blueprint(cliente_bp, url_prefix='/clientes')
    app.register_blueprint(orden_bp, url_prefix='/ordenes')
    app.register_blueprint(auth, url_prefix='/auth')  # ← Registro del blueprint auth

    # Página principal (landing page)
    @app.route('/')
    def index():
        return render_template('landing.html')

    return app

# Punto de entrada principal
if __name__ == '__main__':
    app = create_app()

    # Inicializa la base de datos dentro del contexto de la app
    with app.app_context():
        from database.init_db import init_db
        init_db()

    app.run(debug=True)
