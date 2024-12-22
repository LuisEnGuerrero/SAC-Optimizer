import json
from datetime import datetime
from app.database.config import SessionLocal
from app.database.models import Cliente, Compra

def cargar_clientes():
    session = SessionLocal()
    try:
        # Leer el archivo JSON
        with open("data/clientes.json", "r") as file:
            clientes_data = json.load(file)

        for cliente_data in clientes_data:
            # Extraer las compras del cliente
            compras_data = cliente_data.pop("compras", [])

            # Crear el cliente
            cliente = Cliente(**cliente_data)
            session.add(cliente)
            session.commit()  # Asegurar que el cliente se guarde antes de asociar compras

            for compra_data in compras_data:
                # Asignar el número de documento del cliente a la compra
                compra_data["numero_documento_cliente"] = cliente.numero_documento

                # Convertir la fecha de compra a un objeto datetime
                compra_data["fecha_compra"] = datetime.fromisoformat(compra_data["fecha_compra"])

                # Crear la compra y asociarla al cliente
                compra = Compra(**compra_data)
                session.add(compra)

        # Commit final para guardar todas las compras
        session.commit()
        print("Clientes y compras añadidos con éxito.")

    except Exception as e:
        print(f"Error al cargar clientes: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    cargar_clientes()
