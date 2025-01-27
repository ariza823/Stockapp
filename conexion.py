import mysql.connector  # Asegúrate de importar el módulo correcto

def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",  # Cambia esto si tu base de datos está en otro servidor
            user="root",       # Cambia el usuario si es necesario
            password="1234",       # Cambia la contraseña si es necesario
            database="stockapp"  # Nombre de la base de datos
        )
        print("Conexión exitosa a la base de datos")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Uso de la función
if __name__ == "__main__":
    connection = create_connection()
    if connection:
        # Aquí puedes realizar operaciones con la base de datos
        connection.close()  # No olvides cerrar la conexión