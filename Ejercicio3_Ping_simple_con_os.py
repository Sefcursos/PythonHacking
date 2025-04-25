# Crear el codigo Python necesario para ejecutar el comando del sistema ping (4 paquetes) sobre una IP

# import os
#
# ip = input("Introduce la IP a hacer ping: ")
# os.system(f"ping -n 4 {ip}") # os.system(): permite ejecutar comandos del sistema desde Python
#
# # En Windows es ping -c 4 {ip}

# Opción alternativa si queremos que el script detecte automaticamente si estamos en Windows o Linux

import os
import platform

def hacer_ping(ip):
    sistema = platform.system()

    if sistema == "Windows":
        comando = f"ping -n 1 {ip}"
    else:
        comando = f"ping -c 1 {ip}"

    respuesta = os.system(comando)

    if respuesta == 0:
        print(f"[+] {ip} esta activa")
    else:
        print(f"[-] {ip} no responde")

# Probamos con alguna IP local
hacer_ping("82.98.148.172")