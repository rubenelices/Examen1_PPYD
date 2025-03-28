import queue
import threading

# Cola FIFO para imágenes
almacen_imagenes = queue.Queue()

# Semáforo para sincronizar llegada y procesamiento
imagenes_disponibles = threading.Semaphore(0)

# Contador global para numerar imágenes
contador_imagenes = [0]
contador_lock = threading.Lock()
