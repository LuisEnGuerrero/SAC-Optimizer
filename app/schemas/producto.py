from pydantic import BaseModel
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str
    precio: float
    talla: Optional[str]
    color: Optional[str]
    imagen_url: Optional[str]

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre: Optional[str]
    precio: Optional[float]
    talla: Optional[str]
    color: Optional[str]
    imagen_url: Optional[str]

class ProductoResponse(ProductoBase):
    id: int

    class Config:
        from_attributes = True
