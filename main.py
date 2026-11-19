# --- Aquí cada persona añade el import de su módulo ---
from libros import anadir_libro, listar_libros, borrar_libro
from busqueda import buscar_libro
from datos import guardar_libros, cargar_libros
from estadisticas import mostrar_estadisticas


def mostrar_menu():
    print("\n=== MINI BIBLIOTECA ===")
    # --- Aquí cada persona añade su opción del menú ---
    print("1. Añadir libro")
    print("2. Listar libros")
    print("3. Buscar libro")
    print("4. Guardar libros")
    print("5. Estadísticas")
    print("6. Borrar libro")
    print("0. Salir")


def main():
    biblioteca = cargar_libros()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "0":
            print("¡Hasta pronto!")
            break
        # --- Aquí cada persona añade su elif ---
        elif opcion == "1":
            anadir_libro(biblioteca)
        elif opcion == "2":
            listar_libros(biblioteca)
        elif opcion == "3":
            buscar_libro(biblioteca)
        elif opcion == "4":
            guardar_libros(biblioteca)
        elif opcion == "5":
            mostrar_estadisticas(biblioteca)
        elif opcion == "6":
            borrar_libro(biblioteca)
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
