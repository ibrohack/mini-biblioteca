import os

ARCHIVO = "libros.txt"
SEPARADOR = ";"


def guardar_libros(biblioteca):
    """Guarda los libros en libros.txt, uno por línea: titulo;autor;anio."""
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for libro in biblioteca:
            linea = SEPARADOR.join([libro["titulo"], libro["autor"], libro["anio"]])
            f.write(linea + "\n")
    print(f"Se han guardado {len(biblioteca)} libro(s) en {ARCHIVO}.")
