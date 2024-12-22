from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware
from app.controllers import (
    clientes, 
    get_cliente, 
    exportar_clientes,
    productos,
    reporte_fidelizacion,
    tipo_documento,
    ventas,
)
from app.controllers.flask_admin import flask_app
from app.database.config import Base, engine, SessionLocal
from app.database.models import TipoDocumento
import os

app = FastAPI()

# Agregar número de versión y autor
app.title = "SAC Optimizer"
app.version = "0.1.0"
app.description = "API Desarrollada por: Luis Enrique Guerrero"

@app.get("/")
def read_root():
    return {
            "Bienvenido": "Esta Fast-API está corriendo con Normalidad",
            "Gestión Administrativa": "Para acceder a la gestión administrativa, por favor visite /admin",
            "Documentación": "Para acceder a la documentación de la API, por favor visite /docs",
            }


# Ruta de la base de datos
DB_PATH = os.path.join("app", "database", "sac_optimizer.db")

# Crear la base de datos y poblar datos iniciales si no existe
if not os.path.exists(DB_PATH):
    print("La base de datos no existe. Creándola...")
    try:
        # Crear tablas
        Base.metadata.create_all(bind=engine)
        print("Tablas creadas exitosamente.")

        # Poblar datos iniciales
        session = SessionLocal()
        try:
            # Insertar datos en la tabla TipoDocumento si está vacía
            if not session.query(TipoDocumento).first():
                tipos_documentos = [
                    TipoDocumento(codigo="CC", descripcion="Cédula de Ciudadanía"),
                    TipoDocumento(codigo="TI", descripcion="Tarjeta de Identidad"),
                    TipoDocumento(codigo="NIT", descripcion="Número de Identificación Tributaria"),
                    TipoDocumento(codigo="PAS", descripcion="Pasaporte"),
                ]
                session.add_all(tipos_documentos)
                session.commit()
                print("Datos iniciales para TipoDocumento añadidos con éxito.")
            else:
                print("Datos iniciales ya existen en la tabla 'tipo_documento'.")
        except Exception as e:
            print(f"Error al poblar datos iniciales: {e}")
            session.rollback()
        finally:
            session.close()

    except Exception as e:
        print(f"Error al crear la base de datos: {e}")
        raise RuntimeError("Error en el proceso de creación de la base de datos.")
else:
    print("La base de datos ya existe. No se requiere acción.")


# Configuración del middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Permite el dominio del frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

# Agregar Flask como WSGI middleware
app.mount("/admin", WSGIMiddleware(flask_app))

# Registrar los routers
app.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])  # CRUD de Clientes
app.include_router(get_cliente.router, prefix="/cliente", tags=["Cliente"])
app.include_router(tipo_documento.router, prefix="/tipo_documento", tags=["Tipo de Documento"])
app.include_router(exportar_clientes.router, prefix="/exportar", tags=["Exportar"])
app.include_router(reporte_fidelizacion.router, prefix="/reporte_fidelizacion", tags=["Reportes"])
app.include_router(productos.router, prefix="/productos", tags=["Productos"])
app.include_router(ventas.router, prefix="/ventas", tags=["Ventas"])
