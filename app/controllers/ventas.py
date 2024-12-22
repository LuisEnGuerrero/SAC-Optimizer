from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.config import get_db
from app.database.models import Compra, Historial, Cliente, Producto
from datetime import datetime

router = APIRouter()

@router.post("/")
def registrar_venta(
    venta: dict, 
    db: Session = Depends(get_db)
):
    """
    Registrar una venta y actualizar el historial de cliente.
    """
    cliente_data = venta.get('cliente')
    productos = venta.get('productos', [])
    total = venta.get('total')

    # Validar cliente
    cliente = db.query(Cliente).filter(Cliente.numero_documento == cliente_data.get('numero_documento')).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    # Validar productos
    if not productos:
        raise HTTPException(status_code=400, detail="No se proporcionaron productos para la venta")

    for producto_data in productos:
        producto = db.query(Producto).filter(Producto.id == producto_data['id']).first()
        if not producto:
            raise HTTPException(status_code=404, detail=f"Producto con ID {producto_data['id']} no encontrado")
        
        # Registrar compra
        nueva_compra = Compra(
            numero_documento_cliente=cliente.numero_documento,
            producto_id=producto.id,
            monto=producto.precio * producto_data.get('cantidad', 1)
        )
        db.add(nueva_compra)

    # Registrar historial
    nuevo_historial = Historial(
        numero_documento_cliente=cliente.numero_documento,
        fecha_interaccion=datetime.utcnow(),
        tipo_interaccion=f"Compra registrada. Total: {total}"
    )
    db.add(nuevo_historial)

    # Guardar cambios
    db.commit()
    return {"message": "Venta registrada exitosamente"}
