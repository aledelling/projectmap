from flask import Flask, render_template
from database.db_config import db

# Importa los blueprints (controladores)
from controllers.cliente_controller import cliente_bp
from controllers.orden_controller import orden_bp
from controllers.auth_controller import auth
from controllers.dashboard_controller import dashboard
from controllers.encuesta_controller import comentario_bp
from controllers.factura_controller import factura_bp, init_factura_config

# Importa la clase de configuración
from config.config import Config

def create_app():
    # Crear instancia de Flask
    app = Flask(__name__)
    
    # Cargar configuración
    app.config.from_object(Config)
    
    # Configuración de facturas
    init_factura_config(app)
    
    # Inicializar SQLAlchemy
    db.init_app(app)
    
    # Registrar blueprints
    app.register_blueprint(cliente_bp, url_prefix='/clientes')
    app.register_blueprint(orden_bp, url_prefix='/ordenes')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(dashboard, url_prefix='/dashboard')
    app.register_blueprint(comentario_bp)
    app.register_blueprint(factura_bp)
    
    # Ruta principal
    @app.route('/')
    def index():
        return render_template('landing/landing.html')
    
    # Manejo de errores 404
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404
    
    # Manejo de errores 500
    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500
    
    return app

if __name__ == '__main__':
    # Crear aplicación
    app = create_app()
    
    # Inicializar base de datos dentro del contexto
    with app.app_context():
        from database.init_db import init_db
        init_db()
        print("Base de datos inicializada correctamente")
    
    # Ejecutar aplicación
    print(f"Aplicación iniciada en modo {'debug' if app.config['DEBUG'] else 'producción'}")
    app.run(debug=True)