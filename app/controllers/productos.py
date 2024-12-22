from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.config import SessionLocal
from app.database.models import Producto
from app.schemas.producto import ProductoCreate, ProductoUpdate, ProductoResponse

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProductoResponse)
def create_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    nuevo_producto = Producto(**producto.dict())
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

@router.get("/", response_model=list[ProductoResponse])
def get_productos(skip: int = 0, limit: int = None, db: Session = Depends(get_db)):
    query = db.query(Producto)
    if limit is not None:
        query = query.offset(skip).limit(limit)
    productos = query.all()
    return productos

@router.get("/{producto_id}", response_model=ProductoResponse)
def get_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.put("/{producto_id}", response_model=ProductoResponse)
def update_producto(producto_id: int, producto: ProductoUpdate, db: Session = Depends(get_db)):
    producto_db = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    for key, value in producto.dict(exclude_unset=True).items():
        setattr(producto_db, key, value)
    db.commit()
    db.refresh(producto_db)
    return producto_db

@router.delete("/{producto_id}")
def delete_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(producto)
    db.commit()
    return {"message": "Producto eliminado correctamente"}
