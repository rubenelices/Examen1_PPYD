import time
import random
from recursos import almacen_imagenes, imagenes_disponibles, contador_lock, contador_imagenes
from logger import escribir_log

def satelite(nombre):
    global contador_imagenes

    while True:
        time.sleep(random.uniform(1, 4.5))  # Ritmo aleatorio de llegada

        with contador_lock:
            contador_imagenes[0] += 1
            numero = contador_imagenes[0]

        imagen = f"Imagen {numero} generada por {nombre}"

        almacen_imagenes.put(imagen)
        print(f"[{nombre}] Imagen recibida y almacenada: {imagen}")
        escribir_log(f"[RECEPCIÓN] {imagen}")
        imagenes_disponibles.release()
    