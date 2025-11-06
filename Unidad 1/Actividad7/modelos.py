import json

class Publicacion:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_detalle(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}")

    def to_dict(self):
        raise NotImplementedError("La clase hija debe implementar to_dict")


class Libro(Publicacion):
    def __init__(self, titulo, autor, anio, estado="disponible"):
        super().__init__(titulo, autor, anio)
        self.estado = estado

    def mostrar_detalle(self):
        print(f"[LIBRO] Título: {self.titulo}, Autor: {self.autor}, "
            f"Año: {self.anio}, Estado: {self.estado}")

    def to_dict(self):
        return {
            "tipo": "libro",
            "titulo": self.titulo,
            "autor": self.autor,
            "anio": self.anio,
            "estado": self.estado
        }


class Revista(Publicacion):
    def __init__(self, titulo, autor, anio, numero):
        """Inicializa una nueva Revista."""
        super().__init__(titulo, autor, anio)
        self.numero = numero

    def mostrar_detalle(self):
        print(f"[REVISTA] Título: {self.titulo}, Autor: {self.autor}, "
            f"Año: {self.anio}, Número: {self.numero}")

    def to_dict(self):
        """Convierte el objeto Revista a un diccionario."""
        return {
            "tipo": "revista",
            "titulo": self.titulo,
            "autor": self.autor,
            "anio": self.anio,
            "numero": self.numero
        }


class Usuario:
    def __init__(self, nombre):
        """Inicializa un nuevo Usuario."""
        self.nombre = nombre
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        if isinstance(libro, Libro):
            self.libros_prestados.append(libro)
        else:
            print(f"Error: {libro.titulo} no es un Libro y no puede ser prestado.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
        else:
            print(f"Error: {self.nombre} no tiene el libro {libro.titulo}.")

    def mostrar_detalle(self):
        print(f"Usuario: {self.nombre}")
        if not self.libros_prestados:
            print("  No tiene libros prestados.")
        else:
            print("  Libros prestados:")
            for libro in self.libros_prestados:
                print(f"    - {libro.titulo} (Autor: {libro.autor})")

    def to_dict(self):
        return {
            "nombre": self.nombre,
            # Guardamos solo los títulos para evitar referencias circulares
            "libros_prestados": [libro.titulo for libro in self.libros_prestados]
        }