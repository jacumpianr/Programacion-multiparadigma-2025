from producto import Producto

class Inventario:
    def __init__(self):
        self.__productos = {}  

    def agregar_producto(self, producto: Producto):
        if producto.nombre in self.__productos:
            prod_existente = self.__productos[producto.nombre]
            prod_existente.stock += producto.stock
        else:
            self.__productos[producto.nombre] = producto

    def buscar_producto(self, nombre: str):
        return self.__productos.get(nombre, None)

    def total_valor_inventario(self):
        return sum(p.precio * p.stock for p in self.__productos.values())

    def __len__(self):
        return len(self.__productos)

    def __str__(self):
        if not self.__productos:
            return "Inventario vacío."
        return "\n".join(str(p) for p in self.__productos.values())
