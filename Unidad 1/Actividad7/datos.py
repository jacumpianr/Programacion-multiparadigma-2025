import json
import os
from modelos import Libro, Revista, Usuario
from operaciones import Biblioteca

ARCHIVO_JSON = "datos_biblioteca.json"

def guardar_datos(biblioteca):
    print(f"\nGuardando datos en {ARCHIVO_JSON}...")
    datos = {
        "publicaciones": [],
        "usuarios": []
    }

    # Serializar publicaciones
    for pub in biblioteca.publicaciones:
        datos["publicaciones"].append(pub.to_dict())

    # Serializar usuarios
    for u in biblioteca.usuarios:
        datos["usuarios"].append(u.to_dict())

    try:
        with open(ARCHIVO_JSON, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print("Datos guardados exitosamente.")
    except IOError as e:
        print(f"Error al guardar datos: {e}")

def cargar_datos():
    if not os.path.exists(ARCHIVO_JSON):
        print("No se encontró archivo de datos. Creando nueva biblioteca.")
        return Biblioteca() 

    print(f"Cargando datos desde {ARCHIVO_JSON}...")
    try:
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as f:
            datos = json.load(f)

        bib = Biblioteca()
        mapa_publicaciones = {} 

        for p_data in datos.get("publicaciones", []):
            pub = None
            if p_data.get("tipo") == "libro":
                pub = Libro(p_data["titulo"], p_data["autor"], p_data["anio"], p_data["estado"])
            elif p_data.get("tipo") == "revista":
                pub = Revista(p_data["titulo"], p_data["autor"], p_data["anio"], p_data["numero"])

            if pub:
                bib.agregar_publicacion(pub)
                mapa_publicaciones[pub.titulo] = pub

        # Cargar Usuarios
        for u_data in datos.get("usuarios", []):
            usuario = Usuario(u_data["nombre"])
            bib.agregar_usuario(usuario)

            # Re-enlazar los libros prestados
            for titulo_libro in u_data.get("libros_prestados", []):
                libro_obj = mapa_publicaciones.get(titulo_libro)
                if libro_obj and isinstance(libro_obj, Libro):
                    # Importante: Asignamos el objeto Libro real
                    usuario.libros_prestados.append(libro_obj)

        print("Datos cargados exitosamente.")
        return bib

    except (IOError, json.JSONDecodeError) as e:
        print(f"Error al cargar datos: {e}. Se creará una nueva biblioteca.")
        return Biblioteca()