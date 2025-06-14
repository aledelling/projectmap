# 🛠️ Plataforma de Gestión de Taller Mecánico de Motocicletas

Este repositorio contiene el desarrollo de una plataforma web para la **gestión de taller mecánico de motocicletas**. Está creado por estudiantes del Técnico Laboral como Auxiliar de Sistemas usando **Scrum** como marco de trabajo ágil. La aplicación incluye funciones como facturación, inventario, gestión de clientes, órdenes de trabajo, consulta del estado del vehículo y más.

---

## 📌 Objetivo del Proyecto

Desarrollar una plataforma web con tecnologías accesibles, que permita:

* Administrar la información de clientes y sus motocicletas.
* Controlar órdenes de trabajo y estados de reparación.
* Gestionar inventarios de repuestos.
* Emitir facturas automáticas.
* Registrar usuarios con distintos roles (Técnico, Administrador, Cliente).
* Mejorar la atención al cliente con formularios de contacto y encuestas de satisfacción.
* Ofrecer una vista clara del estado de cada trabajo en curso.

# 🛠️ Moto-Taller – Sistema de Gestión para Talleres de Motocicletas

Moto-Taller es una plataforma web diseñada para digitalizar y optimizar la gestión operativa de talleres de motocicletas. Con ella, se puede administrar clientes, motos, órdenes de trabajo, facturación y encuestas de satisfacción, todo desde una interfaz intuitiva y basada en roles.

---

## 🌟 Visión del Proyecto

### 🎯 Vision Board

| Elemento                | Descripción                                                                                      |
|-------------------------|--------------------------------------------------------------------------------------------------|
| **Meta principal**      | Digitalizar y automatizar los procesos internos de un taller mecánico de motocicletas.          |
| **Problema a resolver** | Falta de control, trazabilidad y eficiencia en talleres que aún usan métodos manuales.          |
| **Clientes clave**      | Propietarios de talleres, técnicos mecánicos, asesores de servicio y clientes de motos.         |
| **Necesidades**         | Registro claro de órdenes, consulta del estado del trabajo, facturación y encuestas de servicio.|
| **Solución propuesta**  | Sistema web modular con acceso controlado, interfaz sencilla y funcionalidades prácticas.        |
| **Ventajas competitivas** | Fácil de usar, accesible desde cualquier navegador, pensado para el entorno real de un taller.  |

---

## 🗺️ Story Mapping

| Fase / Actor          | Cliente                            | Asesor / Técnico                           | Administrador                             |
|----------------------|-------------------------------------|--------------------------------------------|-------------------------------------------|
| **Inicio**           | Consultar el estado de su orden     | Registrar orden de trabajo                 | Crear usuarios y asignar roles            |
| **Gestión**          | Dar feedback sobre el servicio      | Actualizar estado de orden (En progreso, Listo) | Supervisar procesos y ordenes        |
| **Facturación**      | Recibir comprobante digital         | Asociar repuestos y costos                 | Generar y revisar facturas                |
| **Satisfacción**     | Responder encuesta simple           |                                            | Ver métricas de satisfacción              |
| **Inventario**       |                                     | Ver disponibilidad de repuestos            | Cargar o editar stock                     |

---

## 🚀 Producto Mínimo Viable (MVP)

### Objetivo
Tener una primera versión funcional del sistema que permita gestionar clientes y órdenes de trabajo.

### Incluye

- Registro y edición de clientes y motos
- Creación y gestión de órdenes de trabajo
- Cambio de estado de la orden (nuevo, en progreso, terminado)
- Sistema de roles: Administrador, Técnico, Asesor, Cliente
- Visualización del estado de reparación por parte del cliente
- Encuesta de satisfacción simple al finalizar la orden
- Generación de facturas básicas

---

## 📂 Estructura del Proyecto

```
moto-taller/
│
├── app.py                        # Punto de entrada de la aplicación Flask
├── config.py                     # Configuraciones generales (como la conexión a la BD)
├── requirements.txt              # Dependencias del proyecto
├── .gitignore                    # Archivos y carpetas que Git debe ignorar
│
├── controllers/                  # Lógica de control
│   ├── auth_controller.py        # Controlador de autenticación y roles
│   ├── cliente_controller.py     # CRUD para clientes y motos
│   ├── orden_controller.py       # CRUD para órdenes de trabajo
│
├── models/                       # Modelos de datos
│   ├── cliente.py                # Modelo de cliente y motocicleta
│   ├── orden.py                  # Modelo de orden de trabajo y facturación
│
├── database/                     # Base de datos y scripts relacionados
│   ├── init_db.py                # Script de inicialización de la base de datos
│   ├── moto_taller.db            # Archivo de base de datos SQLite
│
├── templates/                    # Plantillas HTML
│   ├── base.html                 # Plantilla base
│   ├── index.html                # Página principal
│
├── static/                       # Archivos estáticos como CSS, JS, Imágenes
│
├── tests/                        # Pruebas unitarias
│   └── test_clientes.py          # Prueba para el módulo de clientes
│
└── docs/                         # Documentación
    ├── arquitectura.md           # Documento de arquitectura del sistema
    ├── base_datos.md             # Documento sobre la base de datos
```

## 👥 Integrantes y Áreas de Trabajo

| Integrante              | Rol Técnico                               | Equipo | Funcionalidades Principales                                                 |
| ----------------------- | ----------------------------------------- | ------ | --------------------------------------------------------------------------- |
| **Alejandro Díaz**      | Scrum Master, Product Owner, Backend Lead | 3      | Gestión de clientes, Órdenes de trabajo, Consulta estado de la moto         |
| **Karen Méndez**        | Frontend Developer                        | 3      | Interfaz de gestión de clientes, órdenes y estado de la moto                |
| **Astrid Figueroa**     | Backend Developer                         | 1      | Lógica del sistema de facturación, gestión de roles de usuario              |
| **Danna Lozano**        | Frontend Developer                        | 1      | Interfaz de usuarios y asignación de roles                                  |
| **Mauricio Martínez**   | Backend Developer                         | 2      | Base de inventarios, lógica de recepción del formulario de contacto         |
| **Erika Forero**        | Frontend Developer, UI/UX Designer        | 2      | Interfaces del formulario de contacto e inventario                          |
| **Andrés Sana**         | Frontend Developer, UI/UX Designer        | 4      | Gestión de datos para encuestas, apoyo backend en marketing                 |
| **Alejandra Justinico** | QA Tester, Frontend Developer             | 4      | Encuesta de satisfacción, pruebas generales, interfaz visual para marketing |

## 👥 Equipos de Trabajo y Funcionalidades

| Equipo | Integrantes                                                                                                                    |
| ------ | ------------------------------------------------------------------------------------------------------------------------------ |
| Todos  | Astrid Figueroa, Danna Lozano, Erika Forero, Mauricio Martínez, Alejandro Díaz, Karen Méndez, Andrés Sana, Alejandra Justinico |

| Equipo | Funcionalidades                                                       |
| ------ | --------------------------------------------------------------------- |
| 1      | Sistema de facturación, Área de usuarios, Definir roles de usuario    |
| 2      | Base de inventarios, Formulario de contacto                           |
| 3      | Gestión de clientes y motos, Órdenes de trabajo, Consulta estado moto |
| 4      | Marketing visual, Encuesta de satisfacción                            |

---

## 👥 Ubicación Áreas de Trabajo

| Integrante              | Rol Técnico                               | Ubicación en el Código                                                                                         | Funcionalidades Principales                                                                 |
| ----------------------- | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Alejandro Díaz**      | Scrum Master, Product Owner, Backend Lead | `controllers/cliente_controller.py`, `controllers/orden_controller.py`, `models/cliente.py`, `models/orden.py` | Gestión de clientes, Órdenes de trabajo, Consulta estado de la moto                         |
| **Karen Méndez**        | Frontend Developer                        | `templates/cliente/`, `templates/orden/`, `templates/estado_moto/`                                             | Interfaz de gestión de clientes, órdenes y estado de la moto                                |
| **Astrid Figueroa**     | Backend Developer                         | `controllers/factura_controller.py`, `models/factura.py`, `controllers/auth_controller.py`                     | Lógica del sistema de facturación, gestión de roles de usuario                              |
| **Danna Lozano**        | Frontend Developer                        | `templates/usuarios/`, `templates/roles/`                                                                      | Interfaz de usuarios y asignación de roles                                                  |
| **Mauricio Martínez**   | Backend Developer                         | `controllers/inventario_controller.py`, `models/inventario.py`, `controllers/contacto_controller.py`           | Base de inventarios, lógica de recepción del formulario de contacto                         |
| **Erika Forero**        | Frontend Developer, UI/UX Designer        | `templates/contacto/`, `templates/inventario/`                                                                 | Interfaces del formulario de contacto e inventario                                          |
| **Andrés Sana**         | Frontend Developer, UI/UX Designer        | `templates/encuesta/`, `static/css/`, `static/js/`, `templates/landing_page/`                                  | Diseño visual de la encuesta de satisfacción, landing page y estilos generales del proyecto |
| **Alejandra Justinico** | QA Tester, Frontend Developer             | `templates/encuesta/`, `templates/landing_page/`, `tests/`                                                     | Encuesta de satisfacción, pruebas generales, interfaz visual para el proyecto               |


(El contenido de cada archivo puede variar. Las rutas se basan en una organización estándar propuesta.)

---

📝 Notas Adicionales
Andrés Sana y Alejandra Justinico son responsables del diseño visual completo del proyecto, incluyendo la estética y experiencia de usuario en el navegador.

El término "marketing" en este contexto se refiere a la presentación visual de la página web, asegurando una interfaz atractiva y funcional para los usuarios.

---

## 📂 Product Backlog

* [x] Definir nombre del proyecto
* [x] Asignar roles
* [x] Sistema de facturación
* [ ] Base de inventarios
* [x] Gestión de clientes y motos
* [ ] Órdenes de trabajo
* [x] Área y roles de usuario
* [ ] Formulario de contacto
* [ ] Diseño y estrategia de marketing
* [ ] Encuesta de satisfacción
* [ ] Consulta del estado de la moto
* [ ] Verificar funcionalidad
* [ ] Entrega del proyecto
---

# 🚀 Sprint Backlog – Proyecto (12 mayo al 8 junio)

Este proyecto se divide en 4 sprints semanales, organizados de menor a mayor complejidad. Todos los equipos participan activamente en cada sprint. A continuación, se detalla la asignación de tareas por equipo y semana:

---

| Integrante              | Rol Técnico                               | Sprint 1 (12–18 mayo)                                      | Sprint 2 (19–25 mayo)                                                      | Sprint 3 (26 mayo–1 junio)                                | Sprint 4 (2–8 junio)                                |
| ----------------------- | ----------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------- |
| **Alejandro Díaz**      | Scrum Master, Product Owner, Backend Lead | Planificación y coordinación general del proyecto          | Desarrollo de backend para gestión de clientes y órdenes de trabajo        | Integración de módulos y pruebas de funcionalidad         | Supervisión de pruebas finales y documentación      |
| **Karen Méndez**        | Frontend Developer                        | Diseño de interfaz para gestión de clientes                | Implementación de interfaz de órdenes de trabajo                           | Integración de interfaces con backend y ajustes de diseño | Pruebas de interfaz y corrección de errores         |
| **Astrid Figueroa**     | Backend Developer                         | Configuración inicial del sistema de facturación           | Desarrollo de lógica para facturación y roles de usuario                   | Integración de facturación con órdenes de trabajo         | Pruebas de facturación y ajustes finales            |
| **Danna Lozano**        | Frontend Developer                        | Diseño de interfaz de usuarios y roles                     | Implementación de formularios de registro y asignación de roles            | Integración de interfaz de usuarios con backend           | Pruebas de interfaz de usuarios y documentación     |
| **Mauricio Martínez**   | Backend Developer                         | Desarrollo de base de inventarios                          | Implementación de lógica para gestión de inventarios y formulario contacto | Integración de inventarios con órdenes de trabajo         | Pruebas de inventarios y ajustes finales            |
| **Erika Forero**        | Frontend Developer, UI/UX Designer        | Diseño de formularios de contacto e inventario             | Implementación de interfaces de contacto e inventario                      | Ajustes de diseño y experiencia de usuario                | Pruebas de interfaz y corrección de errores         |
| **Andrés Sana**         | Frontend Developer, UI/UX Designer        | Diseño de landing page y encuesta de satisfacción          | Implementación de estilos generales y componentes visuales                 | Mejora de UI/UX en módulos existentes                     | Pruebas de experiencia de usuario y ajustes finales |
| **Alejandra Justinico** | QA Tester, Frontend Developer             | Desarrollo de encuesta de satisfacción y pruebas iniciales | Implementación de pruebas generales y ajustes visuales                     | Pruebas de integración y reporte de errores               | Pruebas finales y documentación de pruebas          |

---

🌟 **Objetivo general:** Desarrollar un sistema integral para la gestión de un taller de motocicletas, cubriendo áreas de clientes, inventarios, órdenes, facturación y experiencia de usuario.

---

## 🧰 Tecnologías Usadas

| Tipo       | Tecnología            |
| ---------- | --------------------- |
| Backend    | Python                |
| Base Datos | SQLite                |
| Frontend   | HTML, CSS, JavaScript |

---

## 🔐 Roles de Usuario (Ejemplos)

* **Administrador:** Control total del sistema
* **Técnico:** Actualiza estado de reparaciones
* **Asesor:** Crea órdenes y asigna trabajos
* **Cliente:** Consulta estado y envía encuestas

---

## 💡 Recomendaciones

* Usa **Python** para la lógica del backend (Flask es ideal para empezar).
* Usa **SQLite** como base de datos para evitar complicaciones de instalación.
* Prueba localmente con una base de datos de ejemplo.
* Usa HTML/CSS/JS sin frameworks para entender bien la estructura.
* Implementa CRUD para clientes, motos, inventario y órdenes.
* Versiona tu código usando ramas (`git checkout -b feature/nombre`).

---

## 🗓 Fechas Clave

* Inicio del proyecto: **12 de mayo**
* Entrega final: **8 de junio**

---

## 🤝 Contribuciones

Este proyecto es una oportunidad de aprendizaje colaborativo. Se recomienda usar `Issues` para reportar errores o sugerencias y `Pull Requests` para enviar cambios con revisiones previas.

---

## 📬 Contacto

* **Scrum Master / Product Owner:** Alejandro Díaz
* Contacto: *([jdiazal@cesde.net](mailto:jdiazal@cesde.net))*

---

## 🔗 Conectar el repositorio con Git y Visual Studio Code (Guía para principiantes)

### ✅ Requisitos previos

1. **Cuenta en GitHub:** [https://github.com](https://github.com)
2. **Git instalado:** [https://git-scm.com/](https://git-scm.com/)
3. **Visual Studio Code instalado:** [https://code.visualstudio.com/](https://code.visualstudio.com/)
4. **Extensión de GitHub en VS Code** (opcional pero útil)

---

### 🛠️ 1. Configurar Git por primera vez

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tucorreo@ejemplo.com"
```

---

### 📅 2. Clonar un repositorio desde GitHub en VS Code

1. Abre Visual Studio Code
2. Clic en Source Control o `Ctrl + Shift + G`
3. Clic en **"Clonar repositorio"**
4. Pega la URL del repo: `https://github.com/usuario/repositorio.git`
5. Elige la carpeta donde guardar
6. Abre la carpeta cuando lo solicite

---

### 📌 3. Hacer cambios y subirlos

1. Edita archivos y guarda
2. Ve a Source Control
3. Escribe un mensaje de commit
4. Haz clic en el ✔️ (Commit)
5. Luego clic en los tres puntos > **Push**

---

### 🔄 4. Descargar cambios del equipo

```bash
git pull origin main
```

---

### 🌿 5. Crear y usar ramas

```bash
git checkout -b feature/nombre-funcionalidad
```

Luego:

```bash
git add .
git commit -m "Tu mensaje"
git push origin feature/nombre-funcionalidad
```

---

### 🚚 6. Subir un proyecto local a GitHub

1. Crea un nuevo repo en GitHub
2. En terminal:

```bash
git init
git remote add origin https://github.com/usuario/repositorio.git
git add .
git commit -m "Primer commit"
git branch -M main
git push -u origin main
```

---

🎉 ¡Y listo! Ya puedes trabajar con Git y GitHub desde Visual Studio Code.

