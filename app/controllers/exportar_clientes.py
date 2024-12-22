from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
from app.database.config import SessionLocal
from app.services.export_to_csv import export_to_csv

router = APIRouter()

@router.get("/")
def exportar_clientes():
    """
    Exporta los datos de los clientes a un archivo CSV.
    """
    db = SessionLocal()
    try:
        file_path = export_to_csv(db)
        if not os.path.exists(file_path):
            raise HTTPException(status_code=500, detail="Error al generar el archivo.")
        return FileResponse(
            path=file_path,
            media_type='text/csv',            
            filename="Clientes_RiosDelDesierto.csv",            
        )
    finally:
        db.close()
