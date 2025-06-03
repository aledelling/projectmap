from werkzeug.security import generate_password_hash
import sqlite3

# Ruta relativa a la base de datos
DB_PATH = "database/moto_taller.db"

# Datos del administrador
admin_data = {
    "nombre": "Admin",
    "correo": "admin@mototaller.com",
    "contraseña_hash": generate_password_hash("admin123"),
    "rol_nombre": "Administrador"
}

def crear_admin():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Obtener ID del rol "Administrador"
        cursor.execute("SELECT id FROM roles WHERE nombre = ?", (admin_data["rol_nombre"],))
        rol = cursor.fetchone()
        if not rol:
            print("❌ Error: No existe el rol 'Administrador'.")
            return

        rol_id = rol[0]

        # Verificar si ya existe un usuario con ese correo
        cursor.execute("SELECT id FROM usuarios WHERE correo = ?", (admin_data["correo"],))
        if cursor.fetchone():
            print("⚠️ Ya existe un administrador con ese correo.")
            return

        # Insertar el usuario administrador (columna correcta: contraseña_hash)
        cursor.execute("""
            INSERT INTO usuarios (nombre, correo, contraseña_hash, rol_id)
            VALUES (?, ?, ?, ?)
        """, (admin_data["nombre"], admin_data["correo"], admin_data["contraseña_hash"], rol_id))

        conn.commit()
        print("✅ Administrador creado exitosamente.")
    except Exception as e:
        print(f"❌ Error al crear el administrador: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    crear_admin()
