import csv
import os
from datetime import datetime
from sqlalchemy.orm import Session
from app.database.models import Cliente

def export_to_csv(db: Session) -> str:
    """
    Exporta los datos de los clientes a un archivo CSV con información básica,
    total de compras y fecha de última compra.
    """
    file_path = f"exports/clientes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    # Crear la carpeta de exportación si no existe
    os.makedirs("exports", exist_ok=True)

    # Consultar los datos de los clientes
    clientes = db.query(Cliente).all()

    if not clientes:
        raise Exception("No hay clientes disponibles para exportar.")

    # Escribir los datos en un archivo CSV
    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Número de Documento", "Tipo de Documento", "Nombre", "Apellido", 
            "Correo", "Teléfono", "Total Compras", "Fecha Última Compra"
        ])
        
        for cliente in clientes:
            total_compras = sum(compra.monto for compra in cliente.compras)
            ultima_compra = max(
                (compra.fecha_compra for compra in cliente.compras), default="Sin compras"
            )
            writer.writerow([
                cliente.numero_documento,
                cliente.tipo_documento.codigo,
                cliente.nombre,
                cliente.apellido,
                cliente.correo,
                cliente.telefono,
                total_compras,
                ultima_compra
            ])
    
    return os.path.abspath(file_path)
