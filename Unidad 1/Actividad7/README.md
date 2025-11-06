Sistema de Gestión de Biblioteca

Este es un proyecto de ejemplo en Python que implementa un sistema simple de gestión de biblioteca utilizando principios de Programación Orientada a Objetos (POO).

Descripción del Proyecto

El sistema permite administrar un catálogo de publicaciones (libros y revistas) y un registro de usuarios. Soporta las operaciones básicas de una biblioteca:

Agregar nuevas publicaciones (libros, revistas) al catálogo.

Registrar nuevos usuarios.

Prestar libros a usuarios, actualizando su estado.

Recibir la devolución de libros.

Consultar los libros disponibles.

Guardar y cargar el estado de la biblioteca (catálogo y usuarios) en un archivo datos_biblioteca.json.

Estructura del Código

El proyecto está organizado en cuatro módulos principales, todos ubicados dentro de la carpeta biblioteca/:

modelos.py:

Define las clases de entidad (los "planos" de nuestros datos).

Publicacion: Clase base que define atributos comunes (título, autor, año).

Libro: Hereda de Publicacion. Añade el atributo estado (disponible/prestado).

Revista: Hereda de Publicacion. Añade el atributo numero (para demostrar polimorfismo).

Usuario: Contiene el nombre y una lista de libros_prestados.

operaciones.py:

Define la clase principal de gestión.

Biblioteca: Contiene la lógica de negocio. Administra las listas de publicaciones y usuarios. Incluye métodos para agregar, prestar, devolver y mostrar. Utiliza la encapsulación (métodos privados como _buscar_libro_por_titulo).

datos.py:

Maneja la persistencia de datos.

guardar_datos(biblioteca): Serializa el estado de la biblioteca (listas de objetos) a un archivo JSON.

cargar_datos(): Lee el archivo JSON y "rehidrata" los datos, volviendo a crear los objetos Libro, Revista y Usuario y sus relaciones.

main.py:

Es el punto de entrada de la aplicación.

Contiene la Interfaz de Línea de Comandos (CLI).

Muestra el menú, gestiona la entrada del usuario y llama a los métodos correspondientes de la instancia de Biblioteca.

Demostración de Principios POO

Clases y Objetos: El código está estructurado en clases (Libro, Usuario, Biblioteca, etc.) que generan instancias (objetos) para operar.

Encapsulación: La clase Biblioteca encapsula la lógica de gestión. Métodos como _buscar_libro_por_titulo son privados (convención _) para uso interno.

Herencia: Libro y Revista heredan de la clase base Publicacion, reutilizando código y estableciendo una relación "es un".

Polimorfismo: La Biblioteca almacena Libro y Revista en la misma lista (self.publicaciones). Al llamar a pub.mostrar_detalle() (Opción 6 del menú), Python ejecuta automáticamente la versión correcta del método (la de Libro o la de Revista) según el tipo de objeto.

Instrucciones de Ejecución

Para ejecutar el programa, sigue estos pasos:

Asegúrate de tener Python 3 instalado.

Clona este repositorio o descarga todos los archivos (.py y .md) en una sola carpeta llamada biblioteca.

Abre una terminal o línea de comandos.

Navega dentro de la carpeta biblioteca usando el comando cd.

cd ruta/hacia/el/proyecto/biblioteca


Ejecuta el programa principal:

python main.py


El menú interactivo aparecerá en la consola. La primera vez que se ejecute, creará el archivo datos_biblioteca.json en la misma carpeta al salir (Opción 8).