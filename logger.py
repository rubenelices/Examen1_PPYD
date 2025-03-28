from threading import Lock

log_lock = Lock()

def escribir_log(texto):
    with log_lock:
        with open("registro_imagenes.txt", "a", encoding="utf-8") as f:
            f.write(texto + "\n")
