from werkzeug.security import generate_password_hash
import sqlite3

DB_PATH = "database/moto_taller.db"

tecnico_data = {
    "nombre": "Tecnico1",
    "correo": "tecnico1@mototaller.com",
    "contraseña_hash": generate_password_hash("tecnico123"),
    "rol_nombre": "Técnico"
}

def crear_tecnico():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM roles WHERE nombre = ?", (tecnico_data["rol_nombre"],))
        rol = cursor.fetchone()
        if not rol:
            print("❌ Error: No existe el rol 'Técnico'.")
            return

        rol_id = rol[0]

        cursor.execute("SELECT id FROM usuarios WHERE correo = ?", (tecnico_data["correo"],))
        if cursor.fetchone():
            print("⚠️ Ya existe un técnico con ese correo.")
            return

        cursor.execute("""
            INSERT INTO usuarios (nombre, correo, contraseña_hash, rol_id)
            VALUES (?, ?, ?, ?)
        """, (tecnico_data["nombre"], tecnico_data["correo"], tecnico_data["contraseña_hash"], rol_id))

        conn.commit()
        print("✅ Técnico creado exitosamente.")
    except Exception as e:
        print(f"❌ Error al crear el técnico: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    crear_tecnico()
