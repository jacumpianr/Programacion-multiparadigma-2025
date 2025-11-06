from modelos import Libro, Usuario, Publicacion

class Biblioteca:
    def __init__(self):
        self.publicaciones = []
        self.usuarios = []

    def agregar_publicacion(self, publicacion):
        if isinstance(publicacion, Publicacion):
            self.publicaciones.append(publicacion)
            print(f"Publicación '{publicacion.titulo}' agregada.")
        else:
            print("Error: El objeto no es una Publicación válida.")

    def agregar_usuario(self, usuario):
        if isinstance(usuario, Usuario):
            # Evitar duplicados
            if not self._buscar_usuario_por_nombre(usuario.nombre):
                self.usuarios.append(usuario)
                print(f"Usuario '{usuario.nombre}' agregado.")
            else:
                print(f"Error: El usuario '{usuario.nombre}' ya existe.")
        else:
            print("Error: El objeto no es un Usuario válido.")

    def _buscar_libro_por_titulo(self, titulo):
        for pub in self.publicaciones:
            if isinstance(pub, Libro) and pub.titulo.lower() == titulo.lower():
                return pub
        return None

    def _buscar_usuario_por_nombre(self, nombre):
        for u in self.usuarios:
            if u.nombre.lower() == nombre.lower():
                return u
        return None

    def prestar_libro(self, titulo_libro, nombre_usuario):
        libro = self._buscar_libro_por_titulo(titulo_libro)
        usuario = self._buscar_usuario_por_nombre(nombre_usuario)

        if not libro:
            print(f"Error: Libro '{titulo_libro}' no encontrado.")
            return
        if not usuario:
            print(f"Error: Usuario '{nombre_usuario}' no encontrado.")
            return

        if libro.estado == "disponible":
            libro.estado = "prestado"
            usuario.tomar_prestado(libro)
            print(f"Éxito: '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print(f"Error: '{libro.titulo}' no está disponible.")

    def devolver_libro(self, titulo_libro, nombre_usuario):
        libro = self._buscar_libro_por_titulo(titulo_libro)
        usuario = self._buscar_usuario_por_nombre(nombre_usuario)

        if not libro:
            print(f"Error: Libro '{titulo_libro}' no encontrado.")
            return
        if not usuario:
            print(f"Error: Usuario '{nombre_usuario}' no encontrado.")
            return

        if libro in usuario.libros_prestados:
            libro.estado = "disponible"
            usuario.devolver_libro(libro)
            print(f"Éxito: '{libro.titulo}' devuelto por {usuario.nombre}.")
        else:
            print(f"Error: {usuario.nombre} no tiene '{libro.titulo}' prestado.")

    def mostrar_libros_disponibles(self):
        print("\n--- Libros Disponibles ---")
        encontrados = False
        for pub in self.publicaciones:
            if isinstance(pub, Libro) and pub.estado == "disponible":
                pub.mostrar_detalle()
                encontrados = True
        if not encontrados:
            print("No hay libros disponibles en este momento.")

    def mostrar_todas_las_publicaciones(self):
        print("\n--- Catálogo Completo (Polimorfismo) ---")
        if not self.publicaciones:
            print("No hay publicaciones en el catálogo.")
            return
        for pub in self.publicaciones:
            pub.mostrar_detalle() 

    def mostrar_usuarios_con_libros(self):
        print("\n--- Resumen de Usuarios ---")
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return
        for u in self.usuarios:
            u.mostrar_detalle()