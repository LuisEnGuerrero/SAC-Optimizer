# Deploy SAC-Optimizer

Este documento proporciona una guía paso a paso para desplegar la aplicación SAC-Optimizer, desarrollada con FastAPI y Flask, utilizando Render para el backend y Turso para la base de datos SQLite.

## Prerrequisitos

- Cuenta en [Render](https://render.com/)
- Cuenta en [Turso](https://turso.tech/)
- Git instalado en tu máquina local
- Repositorio de GitHub con el código de la aplicación

## 1. Despliegue del Backend en Render

### Paso 1: Crear un nuevo servicio en Render

1. Inicia sesión en tu cuenta de Render.
2. Haz clic en `New` y selecciona `Web Service`.
3. Conecta tu cuenta de GitHub y selecciona el repositorio `SAC-Optimizer`.
4. Configura los siguientes parámetros:
   - **Name**: `sac-optimizer-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port 8000`
5. Haz clic en `Create Web Service`.

### Paso 2: Configurar variables de entorno

1. En la página del servicio en Render, ve a la sección `Environment` y agrega las siguientes variables de entorno:
   - `DATABASE_URL`: La URL de la base de datos Turso que configuraremos en el siguiente paso.

## 2. Despliegue de la Base de Datos en Turso

### Paso 1: Crear una nueva base de datos en Turso

1. Inicia sesión en tu cuenta de Turso.
2. Crea una nueva base de datos y anota la URL de conexión proporcionada por Turso.

### Paso 2: Configurar la conexión a la base de datos

1. En tu archivo `app/database/config.py`, asegúrate de que la URL de la base de datos se obtenga de la variable de entorno `DATABASE_URL`:

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

2. Asegúrate de que la variable de entorno `DATABASE_URL` en Render esté configurada con la URL de conexión de Turso.

## 3. Relacionar el Backend con la Base de Datos

### Paso 1: Verificar la conexión

1. Asegúrate de que el backend pueda conectarse a la base de datos Turso utilizando la URL proporcionada.
2. Puedes verificar esto ejecutando el backend localmente con la variable de entorno `DATABASE_URL` configurada:

   ```sh
   export DATABASE_URL="URL_DE_TURSO"
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

### Paso 2: Desplegar y probar

1. Una vez que hayas configurado todo correctamente, Render debería desplegar tu aplicación automáticamente.
2. Accede a la URL proporcionada por Render para tu servicio backend y verifica que la aplicación esté funcionando correctamente.

## 4. Notas adicionales

- Asegúrate de que tu base de datos en Turso esté configurada para permitir conexiones desde la IP del servicio Render.
- Puedes utilizar herramientas como Postman o cURL para probar los endpoints de tu API y verificar que todo esté funcionando correctamente.

¡Eso es todo! Ahora tu aplicación SAC-Optimizer debería estar desplegada y funcionando con Render para el backend y Turso para la base de datos.
