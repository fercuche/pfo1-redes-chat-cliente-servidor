import socket
import sqlite3
from datetime import datetime

# Configuración del servidor
HOST = 'localhost'
PORT = 8080

# Inicializar la base de datos
def inicializar_db():
    try:
        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT NOT NULL,
                fecha_envio TEXT NOT NULL,
                ip_cliente TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error al inicializar la base de datos: {e}")
        exit(1)

# Inicializar el socket TCP/IP
def inicializar_socket():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Servidor escuchando en {HOST}:{PORT}...")
        return server_socket
    except socket.error as e:
        print(f"Error al inicializar el socket: {e}")
        exit(1)

# Guardar el mensaje recibido en la base de datos
def guardar_mensaje(contenido, ip_cliente):
    try:
        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
            INSERT INTO mensajes (contenido, fecha_envio, ip_cliente)
            VALUES (?, ?, ?)
        ''', (contenido, timestamp, ip_cliente))
        conn.commit()
        conn.close()
        return timestamp
    except sqlite3.Error as e:
        print(f"Error al guardar el mensaje: {e}")

# Aceptar conexiones y recibir mensajes
def aceptar_conexiones(server_socket):
    while True:
        conn, addr = server_socket.accept()
        print(f"Conexión aceptada desde {addr}")
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                mensaje = data.decode('utf-8')
                print(f"Mensaje recibido de {addr}: {mensaje}")
                timestamp = guardar_mensaje(mensaje, addr[0])
                respuesta = f"Mensaje recibido: {timestamp}"
                conn.sendall(respuesta.encode('utf-8'))

# Main
def main():
    inicializar_db()
    server_socket = inicializar_socket()
    aceptar_conexiones(server_socket)

if __name__ == "__main__":
    main()
