from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
import bcrypt

# Importar el Blueprint desde el archivo rutas_interfaz.py
from routes.rutas_interfaz import interfaz_bp

app = Flask(__name__)

# Configuración para la clave secreta de las sesiones
app.secret_key = 'tu_clave_secreta_aqui'  # Cambia esto por una clave secreta más segura

# Registrar el Blueprint con el prefijo URL '/'
app.register_blueprint(interfaz_bp, url_prefix='/')

# Función para crear la conexión con la base de datos
def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",  # Cambia esto si tu base de datos está en otro servidor
            user="root",       # Cambia el usuario si es necesario
            password="1234",   # Cambia la contraseña si es necesario
            database="stockapp"  # Nombre de la base de datos
        )
        if conn.is_connected():
            print("Conexión exitosa a la base de datos")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Ruta para la página de login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Conexión a la base de datos para verificar las credenciales
        conn = create_connection()
        if conn:
            cursor = conn.cursor(dictionary=True)
            # Consulta para verificar si el usuario existe
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()

            if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')): 
                # Almacenar datos de sesión
                session['user_id'] = user['id']
                session['username'] = user['username']
                
                # Redirigir a la página de inicio si las credenciales son correctas
                flash("Bienvenido, " + username + "!", "success")
                return redirect(url_for('interfaz_bp.inicio'))  # Redirige al Blueprint de inicio
            else:
                # Si las credenciales son incorrectas, se muestra un mensaje de error
                flash("Usuario o contraseña incorrectos", "danger")
        
        else:
            flash("Error en la conexión a la base de datos", "danger")

    return render_template('login.html')

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash("Has cerrado sesión con éxito.", "info")
    return redirect(url_for('login'))  # Redirige al login después de cerrar sesión

# Asegúrate de que el servidor Flask está corriendo en modo debug para facilitar la depuración
if __name__ == '__main__':
    app.run(debug=True)
