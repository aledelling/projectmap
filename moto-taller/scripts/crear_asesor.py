from werkzeug.security import generate_password_hash
import sqlite3

DB_PATH = "database/moto_taller.db"

asesor_data = {
    "nombre": "Asesor1",
    "correo": "asesor1@mototaller.com",
    "contraseña_hash": generate_password_hash("asesor123"),
    "rol_nombre": "Asesor"
}

def crear_asesor():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM roles WHERE nombre = ?", (asesor_data["rol_nombre"],))
        rol = cursor.fetchone()
        if not rol:
            print("❌ Error: No existe el rol 'Asesor'.")
            return

        rol_id = rol[0]

        cursor.execute("SELECT id FROM usuarios WHERE correo = ?", (asesor_data["correo"],))
        if cursor.fetchone():
            print("⚠️ Ya existe un asesor con ese correo.")
            return

        cursor.execute("""
            INSERT INTO usuarios (nombre, correo, contraseña_hash, rol_id)
            VALUES (?, ?, ?, ?)
        """, (asesor_data["nombre"], asesor_data["correo"], asesor_data["contraseña_hash"], rol_id))

        conn.commit()
        print("✅ Asesor creado exitosamente.")
    except Exception as e:
        print(f"❌ Error al crear el asesor: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    crear_asesor()
