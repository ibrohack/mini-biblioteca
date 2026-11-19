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


def listar_libros(biblioteca):
    """Muestra todos los libros numerados o un aviso si no hay ninguno."""
    if not biblioteca:
        print("No hay libros en la biblioteca.")
        return
    for i, libro in enumerate(biblioteca, start=1):
        print(f"{i}. {libro['titulo']} - {libro['autor']} ({libro['anio']})")


def borrar_libro(biblioteca):
    """Muestra los libros, pide el número de uno y lo elimina de la biblioteca."""
    listar_libros(biblioteca)
    if not biblioteca:
        return
    numero = input("Número del libro a borrar: ").strip()
    if not numero.isdigit() or not 1 <= int(numero) <= len(biblioteca):
        print("Número no válido.")
        return
    libro = biblioteca.pop(int(numero) - 1)
    print(f"Libro «{libro['titulo']}» borrado.")
