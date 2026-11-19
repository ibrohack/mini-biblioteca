def buscar_libro(biblioteca):
    """Pide un texto y muestra los libros cuyo título o autor lo contengan
    (sin distinguir mayúsculas de minúsculas)."""
    texto = input("Texto a buscar (título o autor): ").strip().lower()
    resultados = [
        libro for libro in biblioteca
        if texto in libro["titulo"].lower() or texto in libro["autor"].lower()
    ]
    if not resultados:
        print("No se encontraron libros.")
        return
    print(f"Se encontraron {len(resultados)} libro(s):")
    for libro in resultados:
        print(f"- {libro['titulo']} - {libro['autor']} ({libro['anio']})")
