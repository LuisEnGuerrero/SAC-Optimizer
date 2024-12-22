from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class ClienteBase(BaseModel):
    tipo_documento_id: int = Field(..., description="ID del tipo de documento (debe corresponder a un valor válido en la tabla TipoDocumento).")
    numero_documento: str = Field(..., max_length=20, description="Número único del documento.")
    nombre: str = Field(..., max_length=50, description="Nombre del cliente.")
    apellido: str = Field(..., max_length=50, description="Apellido del cliente.")
    correo: EmailStr = Field(..., description="Correo electrónico del cliente.")
    telefono: str = Field(..., max_length=15, description="Número telefónico del cliente.")

class ClienteCreate(ClienteBase):
    """Esquema para creación de clientes."""
    pass

class ClienteUpdate(BaseModel):
    """Esquema para actualización de clientes."""
    nombre: Optional[str] = Field(None, max_length=50)
    apellido: Optional[str] = Field(None, max_length=50)
    correo: Optional[EmailStr] = Field(None)
    telefono: Optional[str] = Field(None, max_length=15)

from pydantic import BaseModel
from typing import List

class ClienteResponse(BaseModel):
    numero_documento: str
    tipo_documento_id: Optional[int]  # Campo obligatorio
    nombre: str
    apellido: str
    correo: str
    telefono: str
    compras: List[dict] = []  # Opcional, inicializa como lista vacía
    historial: List[dict] = []  # Opcional, inicializa como lista vacía

