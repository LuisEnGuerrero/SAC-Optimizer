from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.config import SessionLocal
from app.database.models import Cliente, TipoDocumento
from app.schemas.cliente import ClienteResponse

router = APIRouter()

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=ClienteResponse)
def get_cliente(tipo_documento: str, numero_documento: str, db: Session = Depends(get_db)):
    """
    Obtiene la información completa de un cliente por tipo y número de documento.
    """
    tipo_doc = db.query(TipoDocumento).filter(TipoDocumento.codigo == tipo_documento).first()
    if not tipo_doc:
        raise HTTPException(status_code=404, detail="Tipo de documento no encontrado.")
    
    cliente = db.query(Cliente).filter(
        Cliente.tipo_documento_id == tipo_doc.id,
        Cliente.numero_documento == numero_documento
    ).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")
    
    # Incluye compras e historial en la respuesta
    cliente_data = {
        "tipo_documento_id": cliente.tipo_documento_id,
        "numero_documento": cliente.numero_documento,
        "nombre": cliente.nombre,
        "apellido": cliente.apellido,
        "correo": cliente.correo,
        "telefono": cliente.telefono,
        "compras": [{"id": compra.id, "fecha_compra": compra.fecha_compra, "monto": compra.monto} for compra in cliente.compras],
        "historial": [{"fecha_interaccion": historial.fecha_interaccion, "tipo_interaccion": historial.tipo_interaccion} for historial in cliente.historiales],
    }

    return cliente_data

