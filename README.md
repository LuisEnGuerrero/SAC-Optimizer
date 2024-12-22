# SAC Optimizer

**Versión:** 0.1.0  
**Desarrollado por:** Luis Enrique Guerrero  

---

## Descripción General

SAC Optimizer es una API desarrollada con **FastAPI** que permite la gestión de clientes y sus compras, proporcionando funcionalidades avanzadas para optimizar el servicio de atención al cliente (SAC). Además, incluye una gestión administrativa basada en **Flask** (en desarrollo) para gestionar datos desde una interfaz web.

La API permite:

1. Crear, leer, actualizar y eliminar información de clientes y productos.
2. Consultar información detallada de clientes por tipo y número de documento.
3. Generar reportes de clientes fidelizados en formato Excel.
4. Exportar datos de clientes en varios formatos (CSV, Excel, etc.).

---

## Estructura del Proyecto

```
SAC-Optimizer/
├── app/
│   ├── __init__.py
│   ├── main.py  # Punto de entrada principal de la API
│   ├── controllers/  # Módulos para rutas y gestión administrativa
│   │   ├── __init__.py
│   │   ├── clientes.py
│   │   ├── exportar_clientes.py
│   │   ├── flask_admin.py
│   │   ├── get_cliente.py
│   │   ├── productos.py
│   │   ├── reporte_fidelizacion.py
│   │   └── tipo_documento.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── config.py  # Configuración de la base de datos
│   │   ├── models.py  # Modelos ORM
│   │   ├── sac_optimizer.db  # Base de datos SQLite
│   │   └── setup.py  # Script de inicialización de la base de datos
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── cliente.py
│   │   ├── compra.py
│   │   ├── historial.py
│   │   ├── producto.py
│   │   └── tipo_documento.py
│   └── templates/
│       └── admin/  # Plantillas HTML para gestión administrativa
├── data/
│   ├── add_clientes.py  # Script para cargar clientes
│   ├── add_productos.py  # Script para cargar productos
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   └── test_models.py
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Instalación y Configuración

### Requisitos Previos

- **Python 3.9 o superior**
- **Pip** para la instalación de dependencias
- Entorno virtual recomendado: `venv` o `virtualenv`

### Pasos de Instalación

1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/LuisEnGuerrero/SAC-Optimizer.git
   cd SAC-Optimizer
   ```

2. **Crear un Entorno Virtual**:
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. **Instalar Dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la Base de Datos**:
   - Si la base de datos no existe, se creará automáticamente al iniciar la aplicación.

5. **Iniciar el Servidor**:
   ```bash
   python -m uvicorn app.main:app --reload
   ```

6. **Acceder a la Aplicación**:
   - Documentación interactiva de la API: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Gestión Administrativa (Flask): [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## Endpoints Principales

### Clientes

- **GET /clientes**: Obtener lista de clientes.
- **POST /clientes**: Crear un cliente.
- **GET /clientes/{id}**: Obtener un cliente por ID.
- **PUT /clientes/{id}**: Actualizar un cliente.
- **DELETE /clientes/{id}**: Eliminar un cliente.

### Productos

- **GET /productos**: Obtener lista de productos.
- **POST /productos**: Crear un producto.
- **GET /productos/{id}**: Obtener un producto por ID.
- **PUT /productos/{id}**: Actualizar un producto.
- **DELETE /productos/{id}**: Eliminar un producto.

### Reporte de Fidelización

- **GET /reporte_fidelizacion**: Generar un reporte Excel de clientes con más de 5,000,000 COP en compras en el último mes.

### Exportar Datos

- **GET /exportar/clientes**: Exportar información de clientes en formato CSV/Excel.

---

## Scripts de Datos

### Cargar Clientes
La carpeta /data, contiene arcihvos JSON con datos de prueba que se pueden cargar a la base de datos mediante los scripts de python que aquí mismo se encuentran.

- Archivo: `data/add_clientes.py`
- Uso:
  ```bash
  python -m data.add_clientes
  ```

### Cargar Productos

- Archivo: `data/add_productos.py`
- Uso:
  ```bash
  python -m data.add_productos
  ```

---

## Tecnologías Utilizadas

- **FastAPI**: Framework para crear APIs modernas y de alto rendimiento.
- **Flask**: Framework para la gestión administrativa.
- **SQLite**: Base de datos ligera y sencilla.
- **SQLAlchemy**: ORM para el manejo de la base de datos.
- **Pandas**: Manipulación y generación de reportes.
- **Bootstrap**: Estilizado de plantillas HTML.

---

## Contribución

Si deseas contribuir al proyecto, realiza un fork, crea una rama y envía un pull request con tus cambios.

---

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

