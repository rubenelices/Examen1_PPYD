## EXAMEN PARCIAL 1 DE RUBÉN ELICES
En este repositorio encontraras los codigos del ejercicio práctico del primer examen parcial de programacion paralela y distribuida.

# Simulación Concurrente de Procesamiento de Imágenes Satelitales

Este proyecto simula un sistema concurrente en Python que representa la recepción y procesamiento de imágenes satelitales. Fue desarrollado como caso práctico para demostrar el uso de concurrencia, sincronización y estructuras de datos compartidas.

## ¿Qué hace el sistema?

- Simula satélites que envían imágenes de forma aleatoria.
- Simula analistas que procesan esas imágenes con cierto retardo.
- Garantiza que:
  - No se pierda ninguna imagen.
  - Se mantenga el orden de llegada.
  - Se eviten bloqueos y condiciones de carrera.
- Registra todo el flujo en un archivo de texto `registro_imagenes.txt`.

## Estructura del Proyecto

proyecto_imagenes_sat/
├── main.py                 # Script principal que inicia la simulación
├── generador.py            # Lógica de los satélites (productores)
├── procesador.py           # Lógica de los analistas (consumidores)
├── recursos.py             # Recursos compartidos: cola, semáforo, contador
├── logger.py               # Función segura para registrar eventos en un archivo
├── registro_imagenes.txt   # Archivo generado automáticamente (log de eventos)
└── README.md               # Documentación del proyecto

## ¿Cómo ejecutar?
Desde el archivo main ejecuta el codigo.
Para detener la simulacion simplemente presiona Ctrl+C, si no, será infinita.

