import json
import os

class Tarea:
    """
    Clase base que representa una tarea estándar.
    Aplica ENCAPSULACIÓN: Los atributos principales son "privados" (prefijo _)
    y se accede a ellos mediante propiedades.
    """
    def __init__(self, id, texto, descripcion):
        self._id = id
        self._texto = texto
        self._descripcion = descripcion
        self._completada = False
        self.tipo = "normal"  

    @property
    def id(self):
        return self._id

    @property
    def texto(self):
        return self._texto

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def completada(self):
        return self._completada

    def marcar_completa(self):
        """Marca la tarea como completada."""
        self._completada = True

    def __str__(self):
        """Representación en string."""
        estado = "Exito" if self.completada else "Fallo"
        return f"[{estado}] ID: {self.id} | {self.texto}"

    def mostrar_info(self):
        """
        Método base para mostrar la información.
        Será sobrescrito por clases hijas (Polimorfismo).
        """
        print(self)
        if self.descripcion:
            print(f"    Descripción: {self.descripcion}")

    def a_diccionario(self):
        """Convierte el objeto Tarea en un diccionario para guardar en JSON."""
        return {
            "id": self.id,
            "texto": self.texto,
            "descripcion": self.descripcion,
            "completada": self.completada,
            "tipo": self.tipo
        }


class TareaUrgente(Tarea):
    """
    Clase hija que representa una tarea urgente.
    Aplica HERENCIA.
    """
    def __init__(self, id, texto, descripcion, prioridad):
        # Llama al constructor de la clase padre
        super().__init__(id, texto, descripcion)
        self._prioridad = prioridad
        self.tipo = "urgente"  

    @property
    def prioridad(self):
        return self._prioridad

    def mostrar_info(self):
        """
        Sobrescribe el método de la clase padre para añadir la prioridad.
        Esto es POLIMORFISMO.
        """
        print(f"{super().__str__()} [PRIORIDAD: {self.prioridad.upper()}]")
        if self.descripcion:
            print(f"    Descripción: {self.descripcion}")

    def a_diccionario(self):
        """
        Sobrescribe el método de la clase padre para añadir la prioridad
        al diccionario que se guardará en JSON.
        """
        # Obtiene el diccionario base del padre
        dic_base = super().a_diccionario()
        # Añade el atributo específico de esta clase
        dic_base["prioridad"] = self.prioridad
        return dic_base


class GestorTareas:
    """
    Clase que administra la lista de tareas.
    Maneja la lógica de negocio y la persistencia.
    """
    def __init__(self, archivo_datos="tareas.json"):
        self._tareas = []
        self._siguiente_id = 1
        self._archivo_datos = archivo_datos
        self.cargar_tareas()

    def _actualizar_siguiente_id(self):
        """Calcula el siguiente ID basado en las tareas cargadas."""
        if self._tareas:
            # Busca el ID más alto y le suma 1
            max_id = max(t.id for t in self._tareas)
            self._siguiente_id = max_id + 1
        else:
            self._siguiente_id = 1

    def agregar_tarea(self, texto, descripcion, tipo="normal", prioridad=None):
        """
        Crea y añade una nueva tarea a la lista.
        Decide qué tipo de objeto crear.
        """
        id_nueva = self._siguiente_id
        if tipo == "urgente" and prioridad:
            tarea = TareaUrgente(id_nueva, texto, descripcion, prioridad)
        else:
            tarea = Tarea(id_nueva, texto, descripcion)

        self._tareas.append(tarea)
        self._siguiente_id += 1
        print(f"\nTarea '{texto}' (ID: {id_nueva}) agregada exitosamente.")

    def listar_tareas(self):
        """
        Muestra todas las tareas.
        Aquí ocurre el POLIMORFISMO en acción:
        Llama a `t.mostrar_info()` sin saber si 't' es una Tarea
        o una TareaUrgente. Python ejecuta la versión correcta.
        """
        if not self._tareas:
            print("\nℹNo hay tareas registradas.")
            return

        print("\n--- Listado de Tareas ---")
        for t in self._tareas:
            t.mostrar_info()
            print("-" * 20)  # Separador

    def _buscar_tarea(self, id_tarea):
        """Método auxiliar (privado) para encontrar una tarea por su ID."""
        for t in self._tareas:
            if t.id == id_tarea:
                return t
        return None

    def marcar_completa(self, id_tarea):
        """Busca una tarea y la marca como completada."""
        tarea = self._buscar_tarea(id_tarea)
        if tarea:
            tarea.marcar_completa()
            print(f"\nTarea ID {id_tarea} marcada como completada.")
        else:
            print(f"\nError: No se encontró la tarea con ID {id_tarea}.")

    def eliminar_tarea(self, id_tarea):
        """Busca una tarea y la elimina de la lista."""
        tarea = self._buscar_tarea(id_tarea)
        if tarea:
            self._tareas.remove(tarea)
            print(f"\nTarea ID {id_tarea} eliminada.")
        else:
            print(f"\nError: No se encontró la tarea con ID {id_tarea}.")


    def guardar_tareas(self):
        """Convierte la lista de objetos a JSON y la guarda en un archivo."""
        try:
            datos_para_json = [t.a_diccionario() for t in self._tareas]
            with open(self._archivo_datos, 'w', encoding='utf-8') as f:
                json.dump(datos_para_json, f, indent=4)
            print("\nTareas guardadas exitosamente.")
        except IOError as e:
            print(f"\nError al guardar el archivo: {e}")

    def cargar_tareas(self):
        """Carga las tareas desde el archivo JSON y recrea los OBJETOS."""
        if not os.path.exists(self._archivo_datos):
            print("ℹNo se encontró archivo de datos. Empezando de cero.")
            return

        try:
            with open(self._archivo_datos, 'r', encoding='utf-8') as f:
                datos = json.load(f)

            self._tareas = []
            for item in datos:
                if item.get('tipo') == 'urgente':
                    tarea = TareaUrgente(
                        item['id'],
                        item['texto'],
                        item.get('descripcion', ''),
                        item.get('prioridad', 'alta') 
                    )
                else:
                    tarea = Tarea(
                        item['id'],
                        item['texto'],
                        item.get('descripcion', '')
                    )
                
                if item.get('completada', False):
                    tarea.marcar_completa()
                
                self._tareas.append(tarea)

            self._actualizar_siguiente_id()
            print(f"{len(self._tareas)} tareas cargadas desde '{self._archivo_datos}'.")
        
        except json.JSONDecodeError:
            print(f"Error: El archivo '{self._archivo_datos}' está corrupto.")
        except IOError as e:
            print(f"Error al cargar el archivo: {e}")


# --- Menú Interactivo (Función Principal) ---

def mostrar_menu():
    """Imprime el menú de opciones."""
    print("\n--- Sistema de Gestión de Tareas ---")
    print("1. Agregar Tarea Normal")
    print("2. Agregar Tarea Urgente")
    print("3. Listar Tareas")
    print("4. Marcar Tarea como Completada")
    print("5. Eliminar Tarea")
    print("6. Guardar y Salir")
    print("-------------------------------------")

def main():
    """Función principal que ejecuta el bucle del programa."""
    gestor = GestorTareas() 

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            texto = input("Texto de la tarea: ")
            desc = input("Descripción (opcional): ")
            gestor.agregar_tarea(texto, desc)

        elif opcion == '2':
            texto = input("Texto de la tarea urgente: ")
            desc = input("Descripción (opcional): ")
            prioridad = input("Prioridad (ej: Alta, Media, Baja): ")
            gestor.agregar_tarea(texto, desc, tipo="urgente", prioridad=prioridad)

        elif opcion == '3':
            gestor.listar_tareas()

        elif opcion == '4':
            try:
                id_tarea = int(input("ID de la tarea a completar: "))
                gestor.marcar_completa(id_tarea)
            except ValueError:
                print("Error: Debe ingresar un ID numérico.")

        elif opcion == '5':
            try:
                id_tarea = int(input("ID de la tarea a eliminar: "))
                gestor.eliminar_tarea(id_tarea)
            except ValueError:
                print("Error: Debe ingresar un ID numérico.")

        elif opcion == '6':
            gestor.guardar_tareas()
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Punto de entrada del script
if __name__ == "__main__":
    main()