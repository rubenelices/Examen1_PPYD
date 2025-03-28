import threading
import time
from generador import satelite
from procesador import analista

satellites = ["SAT-1", "SAT-2", "SAT-3"]
analistas = ["Analista-1", "Analista-2", "Analista-3"]

def main():
    for nombre in satellites:
        threading.Thread(target=satelite, args=(nombre,), daemon=True).start()

    for nombre in analistas:
        threading.Thread(target=analista, args=(nombre,), daemon=True).start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nSimulación finalizada.")

if __name__ == "__main__":
    main()
