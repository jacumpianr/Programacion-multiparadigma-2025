# Proyecto: Clase Libro (POO en Python)

## Objetivo
Aplicar los fundamentos de Programación Orientada a Objetos (POO) creando una clase `Libro`, instanciando objetos y manipulando su estado.

---

## Diseño de la clase

- **Atributos de instancia:**
  - `titulo`: nombre del libro.
  - `autor`: nombre del autor.
  - `anio_publicacion`: año en que se publicó.
  - `prestado`: indica si el libro está prestado (inicialmente `False`).

- **Atributo de clase:**
  - `biblioteca`: nombre compartido por todos los libros (`"Biblioteca Central"`).

- **Métodos:**
  - `__init__`: inicializa los atributos.
  - `prestar()`: cambia el estado a prestado.
  - `devolver()`: marca el libro como devuelto.
  - `mostrar_estado()`: muestra toda la información del libro.

---

## 💻 Ejecución
Para ejecutar el programa:

```bash
python main.py