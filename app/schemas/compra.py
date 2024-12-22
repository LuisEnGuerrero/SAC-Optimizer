from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CompraBase(BaseModel):
    cliente_id: str = Field(..., max_length=20, description="Número de documento del cliente asociado.")
    fecha: datetime = Field(..., description="Fecha de la compra.")
    monto: float = Field(..., gt=0, description="Monto total de la compra.")

class CompraCreate(CompraBase):
    """Esquema para la creación de compras."""
    pass

class CompraUpdate(BaseModel):
    """Esquema para la actualización de compras."""
    fecha: Optional[datetime] = Field(None, description="Nueva fecha de la compra.")
    monto: Optional[float] = Field(None, gt=0, description="Nuevo monto de la compra.")

class CompraResponse(CompraBase):
    """Esquema para la respuesta de compras."""
    id: int = Field(..., description="ID único de la compra.")

    class Config:
        from_attributes = True
