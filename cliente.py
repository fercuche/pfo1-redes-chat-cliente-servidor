import socket

# Configuración del cliente
HOST = 'localhost'
PORT = 5000

def main():
    # Inicializar el socket del cliente
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        print(f"Conectado al servidor {HOST}:{PORT}")
    except socket.error as e:
        print(f"Error de conexión: {e}")
        return

    # Enviar múltiples mensajes hasta escribir 'exito'
    try:
        while True:
            mensaje = input("Ingrese un mensaje (o escriba 'exito' para salir): ")
            if mensaje.lower() == 'exito':
                print("Finalizando conexión...")
                break
            client_socket.sendall(mensaje.encode('utf-8'))
            respuesta = client_socket.recv(1024)
            print(f"Respuesta del servidor: {respuesta.decode('utf-8')}")
    except Exception as e:
        print(f"Error durante la comunicación: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
