# Crear un menú con opciones (ej. “1. Suma, 2. Resta, 3. Salir”) usando while.
opcion = ""

while opcion != '3':
    print("\nMenú de Opciones")
    print("1. Suma")
    print("2. Resta")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == '1':
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        suma = num1 + num2
        print (f"La suma de los números es: {suma}")
    elif opcion == '2':
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resta = num1 - num2
        print (f"La resta de los números es: {resta}")
    elif opcion == '3':
        print("Saliendo del programa")