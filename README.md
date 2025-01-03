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

## Gestión Administrativa Mediante FastAPI y Flask:

FastAPI genera automáticamente documentación interactiva para la API, lo que facilita la exploración y prueba de los endpoints disponibles.

**Acceder a la Documentación Interactiva**:
   - Una vez que el servidor esté en funcionamiento, en el navegador web:
   - Navegar a `http://127.0.0.1:8000/docs` para acceder a la documentación generada con **Swagger UI**.

**Explorar y Probar Endpoints**:
   - En la interfaz de **Swagger UI**, se puede ver una lista de todos los endpoints disponibles en la API.
   - Cada endpoint incluye información sobre los métodos HTTP soportados (GET, POST, PUT, DELETE), parámetros requeridos y posibles respuestas.

**Consultar Esquemas de Datos**:
   - La documentación también incluye detalles sobre los esquemas de datos utilizados en la API.
   - Se puede ver la estructura de los modelos de datos, incluyendo los campos requeridos y sus tipos, lo que facilita la comprensión de cómo interactuar con la API.

**Actualizar la Documentación**:
   - Cada vez que se realicen cambios en la API (nuevos endpoints, cambios en los modelos de datos, etc.), la documentación se actualizará automáticamente.
   - Solo basta con reiniciar el servidor para reflejar los cambios en la documentación.


### Modulo de Gestión mediente Flask.


**Acceder a la Página de Gestión**:
   - Una vez que el servidor esté en funcionamiento, en el navegador web:
   - Navegar a `http://127.0.0.1:8000/admin` para acceder a la documentación generada con **Flask**.

**Formularios de Fácil Uso**:
   - En la interfaz de **Flask**, se puede ver una lista de todos los CRUDs disponibles mediante plantillas.
   - Cada CRUD incluye información sobre los métodos soportados (GET, POST, PUT, DELETE), como botones de acción en cada formulario para una gestión de datos eficiente y ágil.

**Actualización de Datos**:
   - Para cada CRUD se generaron las plantillas adecuadas en forma de Formulario con estilo Bootstrap.
   - La gestión de los datos, tanto de Clientes, como de Productos, Compras o Ventas y el Historial, pueden ser actualizados y alimentados de forma manual, respetando la estructura de los datos de forma sencilla.
   
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
## Arquitectura de Software

La estructura del proyecto SAC-Optimizer sigue una arquitectura modular basada en componentes. Se procedió a dividir la aplicación en módulos independientes que se encargan de diferentes responsabilidades que brindan grandes ventajas:

1. **Mantenibilidad**: La separación de responsabilidades en diferentes módulos facilita la localización y corrección de errores, así como la implementación de nuevas funcionalidades sin afectar otras partes del sistema.

2. **Escalabilidad**: La arquitectura modular permite escalar la aplicación de manera más sencilla, ya que se pueden añadir nuevos módulos o mejorar los existentes sin necesidad de reestructurar todo el proyecto.

3. **Reusabilidad**: Los módulos pueden ser reutilizados en otros proyectos o en diferentes partes de la misma aplicación, lo que reduce el tiempo de desarrollo y mejora la consistencia del código.

4. **Facilidad de pruebas**: La estructura modular facilita la creación de pruebas unitarias y de integración, ya que cada módulo puede ser probado de manera independiente.

5. **Colaboración**: La división del proyecto en módulos independientes permite que diferentes equipos de desarrollo trabajen en paralelo en distintas partes de la aplicación, mejorando la eficiencia y reduciendo los tiempos de desarrollo.

Esta arquitectura proporciona una estructura clara y organizada que facilita el desarrollo, mantenimiento y escalabilidad de la aplicación.

---
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
- **GET /cliente/{TipoId}{#Id}**: Obtener un cliente por Tipo y Número de documento de Identificación.
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


# Deploy SAC-Optimizer

Este documento proporciona una guía paso a paso para desplegar la aplicación SAC-Optimizer, desarrollada con FastAPI y Flask, utilizando Render para el backend y Turso para la base de datos SQLite.

## Prerrequisitos

- Cuenta en [Render](https://render.com/)
- Cuenta en [Turso](https://turso.tech/)
- Git instalado en tu máquina local
- Repositorio de GitHub con el código de la aplicación

## 1. Despliegue del Backend en Render

### Paso 1: Crear un nuevo servicio en Render

1. Iniciar sesión en la cuenta de Render.
2. Dar clic en `New` y selecciona `Web Service`.
3. Conectar la cuenta de GitHub y seleccionar el repositorio `SAC-Optimizer`.
4. Configurar los siguientes parámetros:
   - **Name**: `sac-optimizer-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port 8000`
5. Dar clic en `Create Web Service`.

### Paso 2: Configurar variables de entorno

1. En la página del servicio en Render, en la sección `Environment`, agregar las siguientes variables de entorno:
   - `DATABASE_URL`: La URL de la base de datos Turso que se configurará en el siguiente paso.

## 2. Despliegue de la Base de Datos en Turso

### Paso 1: Crear una nueva base de datos en Turso

1. Iniciar sesión en la cuenta de Turso.
2. Crear una nueva base de datos y anotar la URL de conexión proporcionada por Turso.

### Paso 2: Configurar la conexión a la base de datos

1. En el archivo `app/database/config.py`, asignar la URL de la base de datos registrada en la variable de entorno `DATABASE_URL`:

   ```python
   import os
   from sqlalchemy import create_engine
   from sqlalchemy.ext.declarative import declarative_base
   from sqlalchemy.orm import sessionmaker

   DATABASE_URL = os.getenv("DATABASE_URL")

   engine = create_engine(DATABASE_URL)
   SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
   Base = declarative_base()
   ```

2. Verificar de que la variable de entorno `DATABASE_URL` en Render esté configurada con la URL de conexión de Turso.

## 3. Relacionar el Backend con la Base de Datos

### Paso 1: Verificar la conexión

1. Validar de que el backend pueda conectarse a la base de datos Turso utilizando la URL proporcionada.
2. Verificar esto ejecutando el backend localmente con la variable de entorno `DATABASE_URL` configurada:

   ```sh
   export DATABASE_URL="URL_DE_TURSO"
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

### Paso 2: Desplegar y probar

1. Una vez configurado todo correctamente, Render debería desplegar la aplicación automáticamente.
2. Acceder a la URL proporcionada por Render para el backend y verificar que la aplicación esté funcionando correctamente.

## 4. Notas adicionales

- Garantizar de que la base de datos en Turso esté configurada para permitir conexiones desde la IP del servicio Render.
- Se Puede utilizar las herramientas de gestión de FastAPI o Flask, así como Postman o cURL para probar los endpoints de tu API y verificar que todo esté funcionando correctamente.

¡Eso es todo! Ahora la aplicación SAC-Optimizer debería estar desplegada y funcionando con Render para el backend y Turso para la base de datos.


