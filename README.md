# Mini Biblioteca

Programa de consola para gestionar una pequeña biblioteca de libros.

## Cómo ejecutarlo

    python main.py

## Participantes

- **Aritz Navarro** (@Aritzz31): libros (`libros.py`, añadir y listar) y búsqueda (`busqueda.py`).
- **Ivan Vivanco** (@ivanvive7): coordinación (repositorio, `.gitignore`, README y esqueleto de `main.py`) y datos (`datos.py`, guardar y cargar).
- **Brayan Romero** (@ibrohack): revisión de los Pull Request y ampliaciones (estadísticas, borrar libro y ordenar por año).

## Estructura del proyecto

    mini-biblioteca/
    ├── main.py       (menú principal)
    ├── libros.py     (añadir y listar libros)
    ├── busqueda.py   (buscar libros)
    ├── datos.py      (guardar y cargar libros en libros.txt)
    ├── README.md     (descripción del proyecto y participantes)
    └── .gitignore    (archivos que Git debe ignorar)

Los libros se guardan en `libros.txt`, que no se sube al repositorio.

## Organización del equipo

| Integrante    | Roles                       | Rama(s)                        |
|---------------|-----------------------------|--------------------------------|
| Ivan Vivanco  | A · Coordinación, D · Datos | `docs/readme`, `feat/datos`    |
| Aritz Navarro | B · Libros, C · Búsqueda    | `feat/libros`, `feat/busqueda` |
| Brayan Romero | Revisión de PR, ampliaciones | `feat/estadisticas`, `feat/borrar-libro`, `feat/ordenar-por-anio` |

Todo el trabajo entra en `main` mediante Pull Request. Brayan Romero revisa y fusiona los PR de las fases de desarrollo e integración.
