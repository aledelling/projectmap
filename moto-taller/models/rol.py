from models.db import get_db_connection

class Rol:
    @staticmethod
    def obtener_todos():
        conn = get_db_connection()
        roles = conn.execute('SELECT * FROM roles').fetchall()
        conn.close()
        return roles

    @staticmethod
    def crear(nombre):
        conn = get_db_connection()
        conn.execute('INSERT INTO roles (nombre) VALUES (?)', (nombre,))
        conn.commit()
        conn.close()
