# Programa que calcule el área de un triángulo, cuadrado o círculo según lo que elija el usuario.

print("Menu de opciones")
print("Área del triángulo - 1")
print("Área del cuadrado - 2")
print("Área del círculo - 3")
opcion = input("Ingrese una opción: ")

if opcion == '1':
    print ("Área del triángulo")
    base = int(input("Ingrese la base del triángulo: "))
    altura = int(input("Ingrese la altura del triángulo: "))
    area = (base * altura) / 2
    print (f"El área del triangulo es: {area}")
elif opcion == '2':
    print ("Área del cuadrado")
    lado = int(input("Ingrese un lado del cuadrado: "))
    area = lado ** 2
    print (f"El área del cuadrado es: {area}")
elif opcion == '3':
    print ("Área del círculo")
    radio = int(input("Ingrese el radio del círculo: "))
    area = 3.1416 * (radio ** 2)
    print (f"El área del círculo es: {area}")
else:
    print ("Opción no disponible.")
