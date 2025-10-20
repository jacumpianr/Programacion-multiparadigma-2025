# Sistema de Gestión de Tareas (Proyecto POO)

Este proyecto es un sistema de gestión de tareas personales desarrollado en Python, ejecutado íntegramente por consola. El objetivo principal es aplicar y demostrar los conceptos fundamentales de la Programación Orientada a Objetos (POO).

## Características

* **Agregar Tareas**: Permite añadir tareas normales y tareas urgentes (con prioridad).
* **Listar Tareas**: Muestra todas las tareas pendientes y completadas, indicando su tipo y prioridad si aplica.
* **Marcar como Completadas**: Cambia el estado de una tarea a "completada".
* **Eliminar Tareas**: Borra una tarea del sistema usando su ID.
* **Persistencia de Datos**: Guarda automáticamente las tareas en un archivo `tareas.json` al salir y las carga al iniciar.

## Diseño y Principios POO Aplicados

El sistema está diseñado siguiendo los pilares de la POO:

### 1. Clases y Objetos

* **`Tarea`**: Es la clase base. Modela una tarea estándar con atributos como `id`, `texto`, `descripcion` y `completada`.
* **`TareaUrgente`**: Es la clase hija. Modela una tarea que, además de lo anterior, tiene una `prioridad`.
* **`GestorTareas`**: Es la clase principal que orquesta la aplicación. Contiene una lista de *objetos* `Tarea` (o `TareaUrgente`) y define los métodos para interactuar con ellos (agregar, listar, etc.).

### 2. Encapsulación

Se protege el estado interno de los objetos:

* En la clase `Tarea`, los atributos (`_id`, `_texto`, `_completada`) se definen como "privados" (usando un guion bajo).
* Se expone el acceso controlado a estos atributos mediante el decorador `@property` (getters).
* La modificación de atributos, como `_completada`, se realiza a través de métodos públicos (`marcar_completa()`), asegurando que el estado del objeto sea coherente.

### 3. Herencia

Se utiliza la herencia para crear una especialización de `Tarea`:

* La clase `TareaUrgente` **hereda** de `Tarea`.
* Esto significa que `TareaUrgente` reutiliza automáticamente todos los atributos y métodos de `Tarea` (`id`, `texto`, `marcar_completa()`, etc.).
* Además, `TareaUrgente` *extiende* la funcionalidad base añadiendo el atributo `_prioridad`.

### 4. Polimorfismo

Se aprovecha la capacidad de los objetos de clases diferentes para responder al mismo mensaje (llamada de método) de formas distintas:

* **Método `mostrar_info()`**:
    * La clase `Tarea` lo define para mostrar su información básica.
    * La clase `TareaUrgente` lo **sobrescribe** (`override`) para incluir también su nivel de prioridad.
* **En la práctica**: Cuando el `GestorTareas` lista las tareas, simplemente llama a `tarea.mostrar_info()` para cada objeto en su lista. No necesita saber si el objeto es una `Tarea` o una `TareaUrgente`; Python automáticamente ejecuta la versión correcta del método según la clase del objeto.
* **Método `a_diccionario()`**: Este método también es polimórfico. Se usa para la persistencia en JSON. La versión de `TareaUrgente` añade la prioridad al diccionario que genera la clase padre.

## Archivo de Datos

* **`tareas.json`**: Este archivo se crea y se actualiza automáticamente en el mismo directorio donde se ejecuta el script. Almacena las tareas en formato JSON para que la información no se pierda entre ejecuciones.

## Instrucciones de Ejecución

1.  Asegúrate de tener Python 3 instalado.
2.  Clona este repositorio o descarga el archivo `gestor_tareas.py`.
3.  Abre una terminal o consola.
4.  Navega hasta el directorio donde se encuentra el archivo.
5.  Ejecuta el programa con el siguiente comando:

    ```bash
    python gestor_tareas.py
    ```

6.  Sigue las instrucciones del menú interactivo en la consola.