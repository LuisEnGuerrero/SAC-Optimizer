from pydantic import BaseModel
from typing import Optional

class TipoDocumentoBase(BaseModel):
    codigo: str
    descripcion: str

class TipoDocumentoCreate(TipoDocumentoBase):
    """Esquema para crear un tipo de documento."""
    pass

class TipoDocumentoUpdate(BaseModel):
    """Esquema para actualizar un tipo de documento."""
    codigo: Optional[str] = None
    descripcion: Optional[str] = None

class TipoDocumentoResponse(TipoDocumentoBase):
    id: int

    class Config:
        from_attributes = True
