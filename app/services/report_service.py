import pandas as pd
import os
from datetime import datetime, timedelta
from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import HTTPException


def generate_fidelization_report(db: Session) -> str:
    """
    Genera un reporte en Excel de clientes con compras superiores a 5 millones de COP
    en el último mes.
    """
    # Fecha límite para considerar las compras
    fecha_limite = datetime.utcnow() - timedelta(days=30)

    # Consulta SQL para obtener los clientes
    query = text("""
    SELECT c.numero_documento, c.nombre, c.apellido, c.correo, c.telefono, SUM(co.monto) as total_compras
    FROM cliente c
    JOIN compra co ON c.numero_documento = co.numero_documento_cliente
    WHERE co.fecha_compra >= :fecha_limite
    GROUP BY c.numero_documento
    HAVING total_compras > 5000000
    """)
    
    # Ejecutar consulta y registrar resultados
    resultados = db.execute(query, {"fecha_limite": fecha_limite}).fetchall()
    print(f"Resultados de la consulta: {resultados}")

    # Validar resultados
    if not resultados:
        raise HTTPException(status_code=204, detail="No hay clientes que cumplan los criterios de fidelización.")
        
    # Crear DataFrame a partir de los resultados
    columnas = ["Número de Documento", "Nombre", "Apellido", "Correo", "Teléfono", "Total Compras"]
    df = pd.DataFrame(resultados, columns=columnas)
    
    # Generar ruta del archivo
    archivo_excel = f"exports/reporte_fidelizacion_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    os.makedirs("exports", exist_ok=True)
    
    # Exportar a archivo Excel
    try:
        df.to_excel(archivo_excel, index=False, sheet_name="Fidelización")
    except Exception as e:
        print(f"Error al generar el archivo Excel: {e}")
        raise HTTPException(status_code=500, detail="Error al generar el archivo Excel.")
    
    # Validar que el archivo fue creado
    if not os.path.isfile(archivo_excel):
        raise HTTPException(status_code=500, detail="El archivo Excel no se generó correctamente.")
    
    # Registrar y devolver la ruta absoluta del archivo
    ruta_completa = os.path.abspath(archivo_excel)
    print(f"Archivo generado en: {ruta_completa}")
    return ruta_completa
