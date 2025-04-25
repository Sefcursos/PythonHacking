# Crear un programa en Python que escanee automaticamente los puertos de un host y muestre cuáles están abiertos.
# Uso de socket y de ipaddress, estructuras de control

# Escribir un script en Python que reciba una dirección IP y escanee del puerto 1 al 100, mostrando cuáles están abiertos.

#BASICO
# import socket
#
# host = input("Introduce una IP: ")
#
# for port in range(1, 101): # Del puerto 1 al 100
#     s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.settimeout(0.5)
#     result = s.connect_ex((host, port))
#     if result == 0:
#         print("f[+] Puerto {port} abierto")
#     s.close()

# Tambien podemos agregarle el porcentaje de progreso.

import socket # Cargamos la librería para conexiones de red, permite crear conexiones de red TCP/IP y realizar escaneos de puertos

def obtener_ip_local():   # Crear una función que detecte automaticamente la IP local del sistema
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Creamos un socket UDP (Aunque no vamos a enviar datos(, simplemente para que nos dé la IP que usaría el sistema para salir a internet
    try:
        s.connect(("8.8.8.8", 80)) # Nos conectamos a un servidor externo (Google DNS)
        ip = s.getsockname()[0] # Obtenemos la IP local usada para salir
    except Exception:
        ip = "127.0.0.1" # En caso de error, usamos localhost como respaldo
    finally:
        s.close() # Cerramos el socket
    return ip # Devolvemos la IP obtenida

def escanear_puertos(ip, inicio=20, fin=1024): # Definimos otra funcion que recibe una IP y un rango de puertos para escanear. Imprime por consola la IP y el rango escanea.
    print(f"[+] Escaneando {ip} desde el puerto {inicio} al {fin}")
    for puerto in range(inicio, fin + 1): # Bucle que recorre todos los puertos desde el 20 hasta el 1024 (ambos inclusive)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Por cada puerto, creamos un nuevo socket TCP y le damos medio segundo de tiempo para responder, asi evitamos que se quede colgado si el puerto no responde.
        s.settimeout(0.5) # Tiempo maximo de espera para cada conexión
        resultado = s.connect_ex((ip, puerto)) # Intentamos conectar a ese puerto
        if resultado == 0: # Si el resultado es 0 significa que el puerto está abierto, así que lo mostramos por pantalla
            print(f"[+] Puerto abierto: {puerto}")
        s.close() # Cerramos el socket después de cada intento

ip_local = obtener_ip_local() # Obtenemos la IP del sistema
escanear_puertos(ip_local) # Llamamos a la función para escanear puertos

