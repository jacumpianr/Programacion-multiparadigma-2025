from modelos import Libro, Revista, Usuario
from operaciones import Biblioteca
from datos import cargar_datos, guardar_datos

def mostrar_menu():
    """Imprime el menú principal de opciones en la consola."""
    print("\n--- Sistema de Gestión de Biblioteca ---")
    print("1. Agregar nueva publicación (Libro/Revista)")
    print("2. Agregar nuevo usuario")
    print("3. Mostrar libros disponibles")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Mostrar catálogo completo (Polimorfismo)")
    print("7. Mostrar usuarios y sus préstamos")
    print("8. Guardar y Salir")
    print("---------------------------------------")

def agregar_publicacion_menu(biblioteca):
    """Maneja la lógica para agregar una nueva publicación."""
    tipo = input("¿Es un 'libro' o 'revista'? ").lower()
    titulo = input("Título: ")
    autor = input("Autor: ")
    try:
        anio = int(input("Año: "))
    except ValueError:
        print("Error: El año debe ser un número.")
        return

    if tipo == 'libro':
        pub = Libro(titulo, autor, anio)
        biblioteca.agregar_publicacion(pub)
    elif tipo == 'revista':
        try:
            numero = int(input("Número de edición: "))
            pub = Revista(titulo, autor, anio, numero)
            biblioteca.agregar_publicacion(pub)
        except ValueError:
            print("Error: El número de edición debe ser un número.")
    else:
        print("Error: Tipo de publicación no válido.")


def agregar_usuario_menu(biblioteca):
    """Maneja la lógica para agregar un nuevo usuario."""
    nombre = input("Nombre del usuario: ")
    if nombre:
        usuario = Usuario(nombre)
        biblioteca.agregar_usuario(usuario)
    else:
        print("Error: El nombre no puede estar vacío.")

def prestar_libro_menu(biblioteca):
    """Maneja la lógica para prestar un libro."""
    titulo_libro = input("Título del libro a prestar: ")
    nombre_usuario = input("Nombre del usuario: ")
    biblioteca.prestar_libro(titulo_libro, nombre_usuario)

def devolver_libro_menu(biblioteca):
    """Maneja la lógica para devolver un libro."""
    titulo_libro = input("Título del libro a devolver: ")
    nombre_usuario = input("Nombre del usuario: ")
    biblioteca.devolver_libro(titulo_libro, nombre_usuario)

def main():
    """
    Función principal que ejecuta el bucle del programa.
    """
    mi_biblioteca = cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-8): ")

        if opcion == '1':
            agregar_publicacion_menu(mi_biblioteca)
        elif opcion == '2':
            agregar_usuario_menu(mi_biblioteca)
        elif opcion == '3':
            mi_biblioteca.mostrar_libros_disponibles()
        elif opcion == '4':
            prestar_libro_menu(mi_biblioteca)
        elif opcion == '5':
            devolver_libro_menu(mi_biblioteca)
        elif opcion == '6':
            mi_biblioteca.mostrar_todas_las_publicaciones()
        elif opcion == '7':
            mi_biblioteca.mostrar_usuarios_con_libros()
        elif opcion == '8':
            # Guardamos el estado actual antes de salir
            guardar_datos(mi_biblioteca)
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()