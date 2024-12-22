from flask import Blueprint, Flask, render_template, request, redirect
import os
from app.database.config import engine
from sqlalchemy.orm import sessionmaker
from app.database.models import Cliente, Producto, Compra, TipoDocumento

# Crear la aplicación Flask
flask_app = Flask(
    __name__,
    static_folder="static",
    template_folder=os.path.join(os.path.dirname(__file__), "../templates")
)

flask_app.config["TEMPLATES_AUTO_RELOAD"] = True
flask_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app/database/sac_optimizer.db"

print(f"Ruta de plantillas configurada: {flask_app.template_folder}")

# Definir un filtro personalizado para formatear la fecha
def format_datetime(value, format="%Y-%m-%dT%H:%M"):
    if value is None:
        return ""
    return value.strftime(format)

# Registrar el filtro personalizado en Jinja2
flask_app.jinja_env.filters['datetime'] = format_datetime

# Cambia la raíz de Flask bajo "/admin"
admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/",
    template_folder=os.path.join(os.path.dirname(__file__), "../templates/admin")
)

template_path = os.path.join(os.path.dirname(__file__), "../templates/admin/index.html")
print(f"Plantilla admin/index.html existe: {os.path.exists(template_path)}")


# Configurar la sesión de SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@admin_bp.route("/")
def index():
    """Página principal del administrador."""
    print(f"Accediendo a la plantilla: admin/index.html desde {os.getcwd()}")
    print("Ruta de plantillas configurada: ", flask_app.template_folder)
    print(f"existe index.html: {os.path.exists('app/templates/admin/index.html')}")
    return render_template("admin/index.html")

@flask_app.route('/test')
def test():
    return "Flask app is running!"

@admin_bp.route("/tipo_documento")
def tipo_documento():
    """Lista todos los tipos de documento."""
    db = SessionLocal()
    try:
        tipos_documento = db.query(TipoDocumento).all()
        return render_template("tipo_documento.html", tipos_documento=tipos_documento)
    finally:
        db.close()

@admin_bp.route("/tipo_documento/nuevo", methods=["GET", "POST"])
def nuevo_tipo_documento():
    db = SessionLocal()
    try:
        if request.method == "POST":
            # Obtener datos del formulario
            data = request.form
            nuevo_tipo_documento = TipoDocumento(
                codigo=data["codigo"],
                descripcion=data["descripcion"]
            )
            db.add(nuevo_tipo_documento)
            db.commit()
            return redirect("/admin/tipo_documento")
        return render_template("form_tipo_documento.html", action="Agregar")
    finally:
        db.close()

@admin_bp.route("/tipo_documento/<int:id>/editar", methods=["GET", "POST"])
def editar_tipo_documento(id):
    db = SessionLocal()
    try:
        tipo_documento = db.query(TipoDocumento).filter(TipoDocumento.id == id).first()
        if request.method == "POST":
            data = request.form
            tipo_documento.codigo = data["codigo"]
            tipo_documento.descripcion = data["descripcion"]
            db.commit()
            return redirect("/admin/tipo_documento")
        return render_template("form_tipo_documento.html", action="Editar", tipo_documento=tipo_documento)
    finally:
        db.close()

@admin_bp.route("/tipo_documento/<int:id>/eliminar", methods=["GET", "POST"])
def eliminar_tipo_documento(id):
    db = SessionLocal()
    try:
        tipo_documento = db.query(TipoDocumento).filter(TipoDocumento.id == id).first()
        if request.method == "POST":
            db.delete(tipo_documento)
            db.commit()
            return redirect("/admin/tipo_documento")
        return render_template("eliminar_tipo_documento.html", tipo_documento=tipo_documento)
    finally:
        db.close()

        
@admin_bp.route("/clientes")
def clientes():
    """Lista todos los clientes."""
    db = SessionLocal()
    try:
        clientes = db.query(Cliente).all()
        return render_template("clientes.html", clientes=clientes)
    finally:
        db.close()

@admin_bp.route("/clientes/nuevo", methods=["GET", "POST"])
def nuevo_cliente():
    db = SessionLocal()
    try:
        if request.method == "POST":
            # Obtener datos del formulario
            data = request.form
            nuevo_cliente = Cliente(
                numero_documento=data["numero_documento"],
                tipo_documento_id=int(data["tipo_documento_id"]),
                nombre=data["nombre"],
                apellido=data["apellido"],
                correo=data["correo"],
                telefono=data["telefono"],
            )
            db.add(nuevo_cliente)
            db.commit()
            return redirect("/clientes")
        tipos_documentos = db.query(TipoDocumento).all()
        return render_template("form_cliente.html", action="Agregar", tipos_documentos=tipos_documentos)
    finally:
        db.close()

@admin_bp.route("/clientes/<numero_documento>/editar", methods=["GET", "POST"])
def editar_cliente(numero_documento):
    db = SessionLocal()
    try:
        cliente = db.query(Cliente).filter(Cliente.numero_documento == numero_documento).first()
        if request.method == "POST":
            data = request.form
            cliente.tipo_documento_id = int(data["tipo_documento_id"])
            cliente.nombre = data["nombre"]
            cliente.apellido = data["apellido"]
            cliente.correo = data["correo"]
            cliente.telefono = data["telefono"]
            db.commit()
            return redirect("/clientes")
        tipos_documentos = db.query(TipoDocumento).all()
        return render_template("form_cliente.html", action="Editar", cliente=cliente, tipos_documentos=tipos_documentos)
    finally:
        db.close()

@admin_bp.route("/clientes/<numero_documento>/eliminar", methods=["GET"])
def eliminar_cliente(numero_documento):
    db = SessionLocal()
    try:
        cliente = db.query(Cliente).filter(Cliente.numero_documento == numero_documento).first()
        if cliente:
            db.delete(cliente)
            db.commit()
        return redirect("/clientes")
    finally:
        db.close()

@admin_bp.route("/productos")
def productos():
    """Lista todos los productos."""
    db = SessionLocal()
    try:
        productos = db.query(Producto).all()
        return render_template("productos.html", productos=productos)
    finally:
        db.close()

@admin_bp.route("/productos/nuevo", methods=["GET", "POST"])
def nuevo_producto():
    db = SessionLocal()
    try:
        if request.method == "POST":
            # Obtener datos del formulario
            data = request.form
            nuevo_producto = Producto(
                nombre=data["nombre"],
                precio=float(data["precio"]),
                talla=data["talla"],
                color=data["color"],
                imagen_url=data["imagen_url"],
            )
            db.add(nuevo_producto)
            db.commit()
            return redirect("/productos")
        return render_template("form_producto.html", action="Agregar")
    finally:
        db.close()

@admin_bp.route("/productos/<int:id>/editar", methods=["GET", "POST"])
def editar_producto(id):
    db = SessionLocal()
    try:
        producto = db.query(Producto).filter(Producto.id == id).first()
        if request.method == "POST":
            data = request.form
            producto.nombre = data["nombre"]
            producto.precio = float(data["precio"])
            producto.talla = data["talla"]
            producto.color = data["color"]
            producto.imagen_url = data["imagen_url"]
            db.commit()
            return redirect("/productos")
        return render_template("form_producto.html", action="Editar", producto=producto)
    finally:
        db.close()

@admin_bp.route("/productos/<int:id>/eliminar", methods=["GET", "POST"])
def eliminar_producto(id):
    db = SessionLocal()
    try:
        producto = db.query(Producto).filter(Producto.id == id).first()
        if request.method == "POST":
            db.delete(producto)
            db.commit()
            return redirect("/productos")
        return render_template("eliminar_producto.html", producto=producto)
    finally:
        db.close()
        
@admin_bp.route("/compras")
def compras():
    """Lista todas las compras."""
    db = SessionLocal()
    try:
        compras = db.query(Compra).all()
        return render_template("compras.html", compras=compras)
    finally:
        db.close()

@admin_bp.route("/compras/nuevo", methods=["GET", "POST"])
def nueva_compra():
    db = SessionLocal()
    try:
        if request.method == "POST":
            # Obtener datos del formulario
            data = request.form
            nueva_compra = Compra(
                numero_documento_cliente=data["numero_documento_cliente"],
                producto_id=int(data["producto_id"]) if data["producto_id"] else None,
                fecha_compra=data["fecha_compra"],
                monto=float(data["monto"]),
            )
            db.add(nueva_compra)
            db.commit()
            return redirect("/compras")
        productos = db.query(Producto).all()
        return render_template("form_compra.html", action="Agregar", productos=productos)
    finally:
        db.close()

@admin_bp.route("/compras/<int:id>/editar", methods=["GET", "POST"])
def editar_compra(id):
    db = SessionLocal()
    try:
        compra = db.query(Compra).filter(Compra.id == id).first()
        if request.method == "POST":
            data = request.form
            compra.numero_documento_cliente = data["numero_documento_cliente"]
            compra.producto_id = int(data["producto_id"]) if data["producto_id"] else None
            compra.fecha_compra = data["fecha_compra"]
            compra.monto = float(data["monto"])
            db.commit()
            return redirect("/compras")
        productos = db.query(Producto).all()
        return render_template("form_compra.html", action="Editar", compra=compra, productos=productos)
    finally:
        db.close()

@admin_bp.route("/compras/<int:id>/eliminar", methods=["GET", "POST"])
def eliminar_compra(id):
    db = SessionLocal()
    try:
        compra = db.query(Compra).filter(Compra.id == id).first()
        if request.method == "POST":
            db.delete(compra)
            db.commit()
            return redirect("/compras")
        return render_template("eliminar_compra.html", compra=compra)
    finally:
        db.close()

# Registra el blueprint en la app Flask
flask_app.register_blueprint(admin_bp)

# Middleware para ajustar SCRIPT_NAME
@flask_app.before_request
def before_request():
    if request.path.startswith('/admin'):
        request.environ['SCRIPT_NAME'] = '/admin'