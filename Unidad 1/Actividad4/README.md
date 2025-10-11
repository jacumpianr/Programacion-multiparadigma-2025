# Sistema de Inventario con Encapsulación en Python

## Descripción
Este proyecto implementa un sistema básico de inventario utilizando los principios de **programación orientada a objetos (POO)** en Python.  
Se aplican conceptos como **encapsulación**, **atributos privados/protegidos**, **getters y setters**, y **métodos especiales** (`__str__`, `__eq__`, `__len__`).

El sistema permite crear productos, almacenarlos en un inventario, modificar precios y stock, calcular el valor total y buscar productos.

---

## Estructura del Proyecto

---

## Clases y Funcionalidades

### Clase `Producto`
Representa un producto individual con atributos encapsulados.

**Atributos:**
- `nombre` (público, str): nombre del producto.  
- `__stock` (privado, int): cantidad disponible, inicia en 0.  
- `_precio` (protegido, float): precio unitario.

**Métodos:**
- `__init__(self, nombre, precio)`: inicializa el producto y valida que el precio sea mayor que 0.  
- `@property stock`: getter para el stock.  
- `@stock.setter`: no permite valores negativos.  
- `@property precio`: getter para el precio.  
- `@precio.setter`: valida que el precio sea mayor que 0.  
- `__str__`: devuelve una representación legible del producto.  
- `__eq__`: compara productos por nombre.

---

### Clase `Inventario`
Administra un conjunto de productos en un diccionario privado.

**Atributos:**
- `__productos` (privado, dict): contiene los productos, usando el nombre como clave.

**Métodos:**
- `__init__(self)`: inicializa el inventario vacío.  
- `agregar_producto(self, producto)`: agrega un producto o actualiza el stock si ya existe.  
- `buscar_producto(self, nombre)`: busca un producto por su nombre y lo retorna si existe.  
- `total_valor_inventario(self)`: calcula el valor total del inventario.  
- `__len__`: devuelve la cantidad de productos distintos.  
- `__str__`: muestra una lista legible de los productos.