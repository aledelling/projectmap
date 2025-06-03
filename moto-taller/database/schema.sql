PRAGMA foreign_keys = ON;

-- Tabla de roles
CREATE TABLE roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE
);

-- Tabla de usuarios
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL UNIQUE,
    contraseña_hash TEXT NOT NULL,
    rol_id INTEGER NOT NULL,
    FOREIGN KEY (rol_id) REFERENCES roles(id)
);

-- Tabla de clientes
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    cedula TEXT NOT NULL UNIQUE,
    celular TEXT,
    correo TEXT
);

-- Tabla de motos
CREATE TABLE motos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    placa TEXT NOT NULL UNIQUE,
    marca TEXT,
    modelo TEXT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- Tabla de repuestos
CREATE TABLE repuestos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    referencia TEXT NOT NULL UNIQUE,
    cantidad INTEGER NOT NULL,
    precio REAL NOT NULL
);

-- Tabla de órdenes de trabajo
CREATE TABLE ordenes_trabajo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    moto_id INTEGER NOT NULL,
    tecnico_id INTEGER,
    descripcion TEXT,
    estado TEXT CHECK (estado IN ('Pendiente', 'En reparación', 'Listo para entrega')) DEFAULT 'Pendiente',
    fecha_entrada DATE NOT NULL,
    fecha_salida DATE,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (moto_id) REFERENCES motos(id),
    FOREIGN KEY (tecnico_id) REFERENCES usuarios(id)
);

-- Tabla de detalles de repuestos usados en cada orden
CREATE TABLE ordenes_repuestos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    orden_id INTEGER NOT NULL,
    repuesto_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    FOREIGN KEY (orden_id) REFERENCES ordenes_trabajo(id),
    FOREIGN KEY (repuesto_id) REFERENCES repuestos(id)
);

-- Tabla de facturas
CREATE TABLE facturas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    orden_id INTEGER NOT NULL,
    fecha_emision DATE NOT NULL,
    subtotal REAL NOT NULL,
    iva REAL NOT NULL,
    total REAL NOT NULL,
    FOREIGN KEY (orden_id) REFERENCES ordenes_trabajo(id)
);

-- Inserción de roles por defecto
INSERT INTO roles (nombre) VALUES 
('Administrador'),
('Técnico'),
('Asesor'),
('Cliente');
