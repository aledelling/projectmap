from werkzeug.security import generate_password_hash
import sqlite3

DB_PATH = "database/moto_taller.db"

cliente_data = {
    "nombre": "Cliente1",
    "correo": "cliente1@mototaller.com",
    "contraseña_hash": generate_password_hash("cliente123"),
    "rol_nombre": "Cliente"
}

def crear_cliente():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM roles WHERE nombre = ?", (cliente_data["rol_nombre"],))
        rol = cursor.fetchone()
        if not rol:
            print("❌ Error: No existe el rol 'Cliente'.")
            return

        rol_id = rol[0]

        cursor.execute("SELECT id FROM usuarios WHERE correo = ?", (cliente_data["correo"],))
        if cursor.fetchone():
            print("⚠️ Ya existe un cliente con ese correo.")
            return

        cursor.execute("""
            INSERT INTO usuarios (nombre, correo, contraseña_hash, rol_id)
            VALUES (?, ?, ?, ?)
        """, (cliente_data["nombre"], cliente_data["correo"], cliente_data["contraseña_hash"], rol_id))

        conn.commit()
        print("✅ Cliente creado exitosamente.")
    except Exception as e:
        print(f"❌ Error al crear el cliente: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    crear_cliente()
