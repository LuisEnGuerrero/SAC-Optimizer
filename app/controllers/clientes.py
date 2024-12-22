from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.config import SessionLocal
from app.database.models import Cliente
from app.schemas.cliente import ClienteCreate, ClienteUpdate, ClienteResponse
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Cliente
@router.post("/", response_model=ClienteResponse)
def create_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    if db.query(Cliente).filter(Cliente.numero_documento == cliente.numero_documento).first():
        raise HTTPException(status_code=400, detail="El cliente ya existe.")
    cliente_data = Cliente(**cliente.dict())
    db.add(cliente_data)
    db.commit()
    db.refresh(cliente_data)
    return cliente_data

# Read all Clientes
@router.get("/", response_model=List[ClienteResponse])
def get_clientes(db: Session = Depends(get_db)):
    clientes = db.query(Cliente).all()
    return clientes

# Update Cliente
@router.put("/{numero_documento}", response_model=ClienteResponse)
def update_cliente(numero_documento: str, cliente_data: ClienteUpdate, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.numero_documento == numero_documento).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")
    for key, value in cliente_data.dict(exclude_unset=True).items():
        setattr(cliente, key, value)
    db.commit()
    db.refresh(cliente)
    return cliente

# Delete Cliente
@router.delete("/{numero_documento}")
def delete_cliente(numero_documento: str, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.numero_documento == numero_documento).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")
    db.delete(cliente)
    db.commit()
    return {"detail": "Cliente eliminado con éxito"}
