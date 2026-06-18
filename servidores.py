import socket
import sys


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind(('0.0.0.0', 5000))
servidor.listen(1)

print("[-] Servidor iniciado. Esperando una conexión en el puerto 5000...")


conexion, direccion = servidor.accept()


print(f"[+] ¡CONEXIÓN DETECTADA CON ÉXITO!")
print(f"[+] El cliente conectado tiene la IP: {direccion[0]}")
print(f"[+] Entró por el puerto aleatorio: {direccion[1]}")


conexion.close()
servidor.close()
print("[-] Servidor cerrado y puerto liberado.")