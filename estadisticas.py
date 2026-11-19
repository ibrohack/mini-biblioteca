def mostrar_estadisticas(biblioteca):
    """Muestra cuántos libros hay y cuál es el más antiguo."""
    print(f"Total de libros: {len(biblioteca)}")
    con_anio = [libro for libro in biblioteca if libro["anio"].isdigit()]
    if not con_anio:
        print("No hay libros con un año válido para calcular el más antiguo.")
        return
    antiguo = min(con_anio, key=lambda libro: int(libro["anio"]))
    print(f"Libro más antiguo: {antiguo['titulo']} - {antiguo['autor']} ({antiguo['anio']})")
