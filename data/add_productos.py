import json
from app.database.config import SessionLocal
from app.database.models import Producto

def load_productos(file_path: str):
    """Carga productos desde un archivo JSON a la base de datos."""
    session = SessionLocal()
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            productos_data = json.load(file)
            for i, producto in enumerate(productos_data, start=1):
                try:
                    # Crear instancia del modelo Producto
                    nuevo_producto = Producto(**producto)
                    session.add(nuevo_producto)
                    print(f"Producto {i} añadido: {producto['nombre']}")
                except Exception as e:
                    print(f"Error al añadir el producto {producto['nombre']}: {e}")
            session.commit()
            print("Todos los productos procesados exitosamente.")
    except Exception as e:
        print(f"Error general al cargar productos: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    load_productos("data/productos.json")
