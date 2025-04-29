# Propuesta Formativa Obligatoria
## TP: Implementación de un Chat Básico Cliente-Servidor con Sockets y Base de Datos

Este proyecto implementa un chat básico entre un **cliente** y un **servidor** utilizando **sockets** y **una base de datos SQLite** para almacenar los mensajes enviados. El servidor escucha conexiones en un puerto específico y almacena los mensajes que recibe junto con la fecha y la dirección IP del cliente. El cliente permite enviar mensajes y muestra las respuestas del servidor.

## Estructura del Proyecto

- `servidor.py`: Script Python que ejecuta el servidor.
- `cliente.py`: Script Python que ejecuta el cliente.
- `ejecutar_chat.bat`: Archivo batch para ejecutar ambos scripts (servidor y cliente) de manera automatizada.
- `mensajes.db`: Base de datos SQLite que almacena los mensajes (se crea al ejecutar el servidor).

## Instrucciones de Uso

### Ejecución desde Windows

#### 1. Ejecutar el archivo `.bat` haciendo clic:
   - Hacer **doble clic** sobre el archivo `ejecutar_chat.bat`.
   - El servidor se iniciará en segundo plano.
   - Luego, el cliente se ejecutará y podrás interactuar con el servidor.
   - Al escribir **"exito"** en el cliente, tanto el cliente como el servidor se cerrarán automáticamente.

#### 2. Ejecutar el archivo `.bat` desde la terminal bash:
   - Abre un terminal bash.
   - Ejecutar el archivo con `cmd.exe /c ejecutar_chat.bat`
   - El servidor se iniciará en segundo plano.
   - Luego, el cliente se ejecutará y podrás interactuar con el servidor.
   - Al escribir **"exito"** en el cliente, tanto el cliente como el servidor se cerrarán automáticamente.
 
