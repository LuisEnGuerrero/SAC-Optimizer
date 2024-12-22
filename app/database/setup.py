from app.database.config import Base, engine, SessionLocal
from app.database.models import TipoDocumento

def recreate_db():
    """
    Elimina y recrea todas las tablas en la base de datos.
    También repuebla la tabla TipoDocumento con datos iniciales.
    """
    print("Recreando la base de datos...")
    try:
        # Eliminar todas las tablas
        Base.metadata.drop_all(bind=engine)
        print("Tablas eliminadas exitosamente.")

        # Crear todas las tablas
        Base.metadata.create_all(bind=engine)
        print("Tablas creadas exitosamente.")

        # Poblar datos iniciales
        session = SessionLocal()
        try:
            # Insertar datos en la tabla TipoDocumento
            tipos_documentos = [
                TipoDocumento(codigo="CC", descripcion="Cédula de Ciudadanía"),
                TipoDocumento(codigo="TI", descripcion="Tarjeta de Identidad"),
                TipoDocumento(codigo="NIT", descripcion="Número de Identificación Tributaria"),
                TipoDocumento(codigo="PAS", descripcion="Pasaporte"),
            ]
            session.add_all(tipos_documentos)
            session.commit()
            print("Datos iniciales para TipoDocumento añadidos con éxito.")
        except Exception as e:
            print(f"Error al poblar datos iniciales: {e}")
            session.rollback()
        finally:
            session.close()

    except Exception as e:
        print(f"Error al recrear la base de datos: {e}")

if __name__ == "__main__":
    recreate_db()
