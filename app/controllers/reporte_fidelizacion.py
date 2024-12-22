from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os 
from sqlalchemy import text
from app.database.config import SessionLocal
from app.services.report_service import generate_fidelization_report

router = APIRouter()


@router.get("/")
def reporte_fidelizacion():
    """
    Genera y descarga el reporte de fidelización de clientes.
    """
    db = SessionLocal()
    try:
        file_path = generate_fidelization_report(db)
        if not os.path.exists(file_path):
            raise HTTPException(status_code=500, detail="Error al generar el reporte.")
        return FileResponse(
            path=file_path,
            media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            filename=os.path.basename(file_path),
        )
    finally:
        db.close()


@router.get("/count")
def get_fidelization_clients_count():
    """
    Devuelve el número de clientes elegibles para fidelización.
    """
    db = SessionLocal()
    try:
        fecha_limite = datetime.utcnow() - timedelta(days=30)
        query = text("""
        SELECT COUNT(*)
        FROM (
            SELECT c.numero_documento
            FROM cliente c
            JOIN compra co ON c.numero_documento = co.numero_documento_cliente
            WHERE co.fecha_compra >= :fecha_limite
            GROUP BY c.numero_documento
            HAVING SUM(co.monto) > 5000000
        ) subquery
        """)
        result = db.execute(query, {"fecha_limite": fecha_limite}).scalar()
        return result
    finally:
        db.close()
