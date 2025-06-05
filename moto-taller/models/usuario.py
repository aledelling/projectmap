from models.db import get_db_connection

class Usuario:
    @staticmethod
    def obtener_todos():
        conn = get_db_connection()
        usuarios = conn.execute('SELECT usuarios.*, roles.nombre AS rol_nombre FROM usuarios JOIN roles ON usuarios.rol_id = roles.id').fetchall()
        conn.close()
        return usuarios

    @staticmethod
    def crear(nombre, correo, contrasena, rol_id):
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO usuarios (nombre, correo, contrasena, rol_id) VALUES (?, ?, ?, ?)',
            (nombre, correo, contrasena, rol_id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def autenticar(correo, contrasena):
        conn = get_db_connection()
        usuario = conn.execute(
            'SELECT * FROM usuarios WHERE correo = ? AND contrasena = ?',
            (correo, contrasena)
        ).fetchone()
        conn.close()
        return usuario

