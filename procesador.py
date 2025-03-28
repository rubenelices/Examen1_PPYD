import time
import random
from recursos import almacen_imagenes, imagenes_disponibles
from logger import escribir_log

def analista(nombre):
    while True:
        imagenes_disponibles.acquire()
        imagen = almacen_imagenes.get()

        print(f"({nombre}) Procesando imagen: {imagen}")
        tiempo_procesado = random.uniform(4, 7)  # Procesamiento más lento
        time.sleep(tiempo_procesado)
        print(f"({nombre}) Finalizó el procesamiento de: {imagen} en {tiempo_procesado:.2f}s")
        escribir_log(f"[PROCESAMIENTO] {imagen} → procesada por {nombre} en {tiempo_procesado:.2f} segundos")
