from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class HistorialBase(BaseModel):
    cliente_id: str = Field(..., max_length=20, description="Número de documento del cliente asociado.")
    fecha_interaccion: datetime = Field(..., description="Fecha de la interacción.")
    tipo_interaccion: str = Field(..., max_length=100, description="Tipo de interacción (e.g., llamada, compra).")

class HistorialCreate(HistorialBase):
    """Esquema para la creación de historiales."""
    pass

class HistorialUpdate(BaseModel):
    """Esquema para la actualización de historiales."""
    fecha_interaccion: Optional[datetime] = Field(None, description="Nueva fecha de la interacción.")
    tipo_interaccion: Optional[str] = Field(None, max_length=100, description="Nuevo tipo de interacción.")

class HistorialResponse(HistorialBase):
    """Esquema para la respuesta de historiales."""
    id: int = Field(..., description="ID único del historial.")

    class Config:
        from_attributes = True
