def anadir_libro(biblioteca):
    """Pide título, autor y año por teclado y añade el libro a la biblioteca."""
    titulo = input("Título: ").strip()
    if not titulo:
        print("El título no puede estar vacío.")
        return
    autor = input("Autor: ").strip()
    anio = input("Año: ").strip()
    biblioteca.append({"titulo": titulo, "autor": autor, "anio": anio})
    print(f"Libro «{titulo}» añadido.")
