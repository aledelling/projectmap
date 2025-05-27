# Importa el módulo sqlite3 para trabajar con bases de datos SQLite
import sqlite3

# Importa herramientas de Flask:
# - g: objeto global que permite almacenar datos durante el ciclo de vida de una solicitud
# - current_app: permite acceder a la instancia actual de la aplicación Flask
from flask import g, current_app

# Importa os en caso de que se necesiten rutas absolutas (aunque aquí no se usa directamente)
import os


# Función para obtener una conexión a la base de datos
def get_db():
    # Verifica si ya hay una conexión guardada en el objeto global 'g'
    if 'db' not in g:
        # Si no existe, crea una nueva conexión a la base de datos
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],  # Usa la ruta del archivo definida en config.py
            detect_types=sqlite3.PARSE_DECLTYPES  # Permite que SQLite detecte automáticamente tipos como datetime
        )
        # Configura la conexión para que devuelva filas como diccionarios (se puede acceder por nombre de columna)
        g.db.row_factory = sqlite3.Row

    # Devuelve la conexión, ya sea la existente o la nueva
    return g.db


# Función para cerrar la conexión a la base de datos
def close_db(e=None):
    # Intenta sacar ('pop') la conexión de la base de datos del contexto global 'g'
    db = g.pop('db', None)

    # Si había una conexión activa, la cierra
    if db is not None:
        db.close()


# Función para inicializar la base de datos (crear tablas)
def init_db():
    # Obtiene una conexión activa a la base de datos
    db = get_db()

    # Abre el archivo 'schema.sql' que contiene las sentencias SQL para crear las tablas
    # current_app.open_resource asegura que se busque el archivo desde la raíz de la aplicación
    with current_app.open_resource('database/schema.sql') as f:
        # Lee el contenido del archivo, lo decodifica como UTF-8 y lo ejecuta como script SQL
        db.executescript(f.read().decode('utf8'))
