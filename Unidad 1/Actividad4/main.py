from producto import Producto
from inventario import Inventario

def main():
    inv = Inventario()

    p1 = Producto("Laptop", 15000)
    p1.stock = 5

    p2 = Producto("Mouse", 250)
    p2.stock = 20

    p3 = Producto("Teclado", 600)
    p3.stock = 10

    p4 = Producto("Laptop", 15000)
    p4.stock = 2  

    inv.agregar_producto(p1)
    inv.agregar_producto(p2)
    inv.agregar_producto(p3)
    inv.agregar_producto(p4)

    print("=== Inventario Actual ===")
    print(inv)
    print("=========================")

    p2.precio = 300  

    print(f"\nValor total del inventario: ${inv.total_valor_inventario():.2f}")

    nombre_buscar = "Mouse"
    encontrado = inv.buscar_producto(nombre_buscar)
    if encontrado:
        print(f"\nProducto encontrado: {encontrado}")
    else:
        print(f"\nProducto '{nombre_buscar}' no encontrado.")

    print("\n¿p1 y p4 son iguales?", p1 == p4)
    print("Numero total de productos distintos:", len(inv))

if __name__ == "__main__":
    main()
