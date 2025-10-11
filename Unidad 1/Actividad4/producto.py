class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        self._precio = precio
        self.__stock = 0  

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise ValueError("El stock no puede ser negativo.")
        self.__stock = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        self._precio = valor

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: ${self._precio:.2f}, Stock: {self.__stock}"

    def __eq__(self, other):
        if isinstance(other, Producto):
            return self.nombre.lower() == other.nombre.lower()
        return False