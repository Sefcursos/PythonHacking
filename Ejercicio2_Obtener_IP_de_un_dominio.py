# Obtener IP de un dominio usando DNS

import socket

dominio = input("Introduce el dominio: ")
ip = socket.gethostbyname(dominio) # Hace la consulta DNS para resolver la IP
print(f"La IP  de {dominio} es {ip}")