import socket
import sys

cliente=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('127.0.0.1', 5000))
print("[+] ¡Nos hemos conectado exitosamente al servidor!")
cliente.close()
print("[-] Conexión terminada.")
