from flask import Blueprint, render_template, session, redirect, url_for

# Crear el Blueprint
interfaz_bp = Blueprint('interfaz_bp', __name__)

# Función para verificar si el usuario está autenticado
def is_authenticated():
    return 'user_id' in session  # Verificamos si el 'user_id' está en la sesión

# Ruta para la página de inicio
@interfaz_bp.route('/inicio')
def inicio():
    if not is_authenticated():
        return redirect(url_for('login'))  # Redirigir al login si no está autenticado
    return render_template('home.html')  # Cambia a la plantilla que corresponda

# Ruta para usuarios
@interfaz_bp.route('/usuarios')
def usuarios():
    if not is_authenticated():
        return redirect(url_for('login'))  # Redirigir al login si no está autenticado
    return render_template('usuario.html')  # Cambia a la plantilla que corresponda

# Ruta para proveedores
@interfaz_bp.route('/proveedores')
def proveedores():
    if not is_authenticated():
        return redirect(url_for('login'))  # Redirigir al login si no está autenticado
    return render_template('proveedores.html')  # Cambia a la plantilla que corresponda

# Ruta para productos
@interfaz_bp.route('/productos')
def productos():
    if not is_authenticated():
        return redirect(url_for('login'))  # Redirigir al login si no está autenticado
    return render_template('producto.html')  # Cambia a la plantilla que corresponda

# Ruta para ventas
@interfaz_bp.route('/ventas')
def ventas():
    if not is_authenticated():
        return redirect(url_for('login'))  # Redirigir al login si no está autenticado
    return render_template('detalle_venta.html')  # Cambia a la plantilla que corresponda

# Ruta para inventario
@interfaz_bp.route('/inventario')
def inventario():
    if not is_authenticated():
        return redirect(url_for('login'))  # Redirigir al login si no está autenticado
    return render_template('inventario.html')  # Cambia a la plantilla que corresponda

# Ruta para agregar un nuevo producto (si existe en tu interfaz)
@interfaz_bp.route('/agregar_producto')
def agregar_producto():
    if not is_authenticated():
        return redirect(url_for('login'))  # Redirigir al login si no está autenticado
    return render_template('agregar_producto.html')  # Cambia a la plantilla que corresponda
