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


def cargar_libros():
    """Lee libros.txt y devuelve la lista de libros.
    Si el archivo no existe, devuelve una lista vacía."""
    biblioteca = []
    if not os.path.exists(ARCHIVO):
        return biblioteca
    with open(ARCHIVO, encoding="utf-8") as f:
        for linea in f:
            partes = linea.rstrip("\n").split(SEPARADOR)
            if len(partes) == 3:
                titulo, autor, anio = partes
                biblioteca.append({"titulo": titulo, "autor": autor, "anio": anio})
    return biblioteca
