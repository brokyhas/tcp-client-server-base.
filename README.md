# tcp-client-server-base.
basic server/cliente
Markdown
# TCP Client-Server Base (Python)

Este es un entorno base de red utilizando la arquitectura **Cliente-Servidor** mediante sockets TCP nativos en Python. Fue desarrollado y probado de manera local en un entorno Linux para comprender los fundamentos del ciclo de vida de una conexión de red (TCP Lifecycle).

El proyecto demuestra cómo un servidor puede abrir un puerto específico del sistema operativo para escuchar peticiones entrantes, y cómo un cliente independiente puede conectarse a él en tiempo real.

---

## 🛠️ Arquitectura del Proyecto

El entorno se divide en dos scripts independientes:

1. **`servidor.py`**: El núcleo que gestiona la infraestructura local.
   * Crea el socket TCP (`AF_INET`, `SOCK_STREAM`).
   * Configura la reutilización de puertos para evitar bloqueos del sistema.
   * Se enlaza a la dirección local (`bind`) en el puerto `5000`.
   * Se queda en modo de escucha (`listen`) y bloquea el flujo con `accept()` hasta recibir un cliente.
   * Captura de forma transparente la IP y el puerto dinámico de origen del cliente conectado.

2. **`cliente.py`**: El nodo emisor.
   * Se inicializa y apunta directamente a la dirección de bucle de retorno o loopback (`127.0.0.1`) en el puerto asignado.
   * Establece un saludo de red (`connect`), confirma el éxito en pantalla y cierra la sesión limpiamente.

---

## 🚀 Instrucciones de Ejecución

Para ejecutar este entorno en tu máquina local (utilizando terminales divididas en VS Code o cualquier emulador de terminal), sigue este orden secuencial estricto:

### 1. Iniciar el Servidor
Levanta el servicio para que se quede escuchando en el puerto configurado:
```bash
python servidor.py
Salida esperada:

Plaintext
[-] Servidor iniciado. Esperando una conexión en el puerto 5000...
2. Ejecutar el Cliente
En una segunda terminal o panel dividido, lanza el script del cliente para golpear el puerto:

Bash
python cliente.py
Salida esperada en la terminal del Cliente:

Plaintext
[+] ¡Nos hemos conectado exitosamente al servidor!
[-] Conexión terminada.
🎯 Resultado en el Servidor
En el instante en que el cliente se conecta, verás al servidor reaccionar e imprimir los metadatos de la conexión antes de liberar el puerto:

Plaintext
[+] ¡CONEXIÓN DETECTADA CON ÉXITO!
[+] El cliente conectado tiene la IP: 127.0.0.1
[+] Entró por el puerto aleatorio: <PUERTO_DINÁMICO>
[-] Servidor cerrado y puerto liberado.
🔒 Próximos Pasos (Enfoque en Ciberseguridad)
Este script sirve como la plantilla estructural de bajo nivel para proyectos de auditoría de redes más avanzados, tales como:

Escáneres de puertos automatizados (Port Scanners).

Herramientas de transferencia de archivos cifrados.

Estructuras de control remoto para entornos controlados de laboratorio.
