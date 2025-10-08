from libro import Libro

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
libro2 = Libro("1984", "George Orwell", 1949)
libro3 = Libro("El principito", "Antoine de Saint-Exupéry", 1943)

libro1.prestar()
libro2.prestar()
libro2.devolver()

libro1.mostrar_estado()
libro2.mostrar_estado()
libro3.mostrar_estado()