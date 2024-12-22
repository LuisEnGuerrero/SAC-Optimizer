from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.config import SessionLocal
from app.database.models import TipoDocumento
from app.schemas.tipo_documento import TipoDocumentoCreate, TipoDocumentoUpdate, TipoDocumentoResponse

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear un nuevo tipo de documento
@router.post("/", response_model=TipoDocumentoResponse)
def create_tipo_documento(tipo_documento: TipoDocumentoCreate, db: Session = Depends(get_db)):
    # Verificar si el código ya existe
    existing = db.query(TipoDocumento).filter(TipoDocumento.codigo == tipo_documento.codigo).first()
    if existing:
        raise HTTPException(status_code=400, detail="El código ya existe.")
    
    nuevo_tipo_documento = TipoDocumento(**tipo_documento.dict())
    db.add(nuevo_tipo_documento)
    db.commit()
    db.refresh(nuevo_tipo_documento)
    return nuevo_tipo_documento

# Obtener todos los tipos de documento
@router.get("/", response_model=list[TipoDocumentoResponse])
def get_tipos_documento(db: Session = Depends(get_db)):
    return db.query(TipoDocumento).all()

# Actualizar un tipo de documento
@router.put("/{tipo_documento_id}", response_model=TipoDocumentoResponse)
def update_tipo_documento(tipo_documento_id: int, tipo_documento: TipoDocumentoUpdate, db: Session = Depends(get_db)):
    tipo_doc = db.query(TipoDocumento).filter(TipoDocumento.id == tipo_documento_id).first()
    if not tipo_doc:
        raise HTTPException(status_code=404, detail="Tipo de documento no encontrado.")
    
    for key, value in tipo_documento.dict(exclude_unset=True).items():
        setattr(tipo_doc, key, value)
    
    db.commit()
    db.refresh(tipo_doc)
    return tipo_doc

# Eliminar un tipo de documento
@router.delete("/{tipo_documento_id}", response_model=dict)
def delete_tipo_documento(tipo_documento_id: int, db: Session = Depends(get_db)):
    tipo_doc = db.query(TipoDocumento).filter(TipoDocumento.id == tipo_documento_id).first()
    if not tipo_doc:
        raise HTTPException(status_code=404, detail="Tipo de documento no encontrado.")
    
    db.delete(tipo_doc)
    db.commit()
    return {"detail": "Tipo de documento eliminado exitosamente."}
