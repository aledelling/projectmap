# config.py
# Importa el módulo 'os', que permite interactuar con el sistema operativo,
# por ejemplo, para trabajar con rutas de archivos de forma segura
import os

# Define la ruta base del proyecto, obteniendo el directorio actual del archivo
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define una clase de configuración para la aplicación Flask
class Config:
    # Define la ruta absoluta del archivo de la base de datos SQLite
    DATABASE = os.path.join(BASE_DIR, 'moto_taller.db')

    # Define la clave secreta para la aplicación Flask, usada por ejemplo para sesiones y seguridad
    # Toma la clave de una variable de entorno si existe, si no, usa una por defecto
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-secreta-predeterminada'

    # Habilita el modo de depuración (útil durante el desarrollo)
    DEBUG = True
