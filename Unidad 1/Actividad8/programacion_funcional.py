# Parte 1: Identificar y analizar
# Indicar si:
# - Es pura o impura
# - Por que? (identificar el problema especifico si es impura)
# - Como convertirla en pura (Si aplica)

# Funcion A
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

# Funcion B
contador = 0
def siguiente_id():
    global contador
    contador += 1
    return f"ID--{contador}"

# Funcion C
def agregar_fecha(registro):
    from datetime import datetime
    registro['fecha'] = datetime.now().isoformat()
    return registro

# Funcion D
def filtrar_positivos(numeros):
    return [n for n in numeros if n > 0]

# Funcion E
import random
def mezclar_lista(lista):
    random.shuffle(lista)
    return lista

# Parte 2: Conversion de paradigmas
# Usar funciones puras
# No modificar las estructuras de datos originales
# Aprovechar funciones como ciudadanos de primera clase

# def procesar_ventas(ventas):
#    """
#    Codigo imperativo a convertir.
#    Entrada: Lista de diccionarios con ventas
#    Proceso:
#    1. Filtrar ventanas mayores a $100
#    2. Aplicar el 15% de impuesto
#    3. Calcular el total
#    """
#    resultado = []
#    total = 0
#
#    for venta in ventas:
#        if venta['monto'] > 100:
#            monto_con_impuesto = venta['monto'] * 1.15
#            nueva_venta = {
#                'id': venta['id'],
#                'monto_original': venta['monto'],
#                'monto_final': monto_con_impuesto
#            }
#            resultado.append(nueva_venta)
#            total += monto_con_impuesto
#    return resultado, total 
#

from functools import reduce

def procesar_ventas(ventas):
    # Filtrar ventas mayores a 100 
    filtrar = lambda venta: venta['monto'] > 100
    ventas_filtradas = list(filter(filtrar, ventas))

    # Aplicar impuesto del 15 %
    aplicar_impuesto = lambda venta: {
        'id': venta['id'],
        'monto_original': venta['monto'],
        'monto_final': venta['monto'] * 1.15
    }
    ventas_procesadas = list(map(aplicar_impuesto, ventas_filtradas))

    # Calcular el total con reduce
    total = reduce(lambda acc, v: acc + v['monto_final'], ventas_procesadas, 0)

    return ventas_procesadas, total


ventas = [ 
    {'id': 1, 'monto': 50},
    {'id': 2, 'monto': 150},
    {'id': 3, 'monto': 200},
    {'id': 4, 'monto': 80},
    {'id': 5, 'monto': 300}
]

procesadas, total = procesar_ventas(ventas)

print(procesadas)
print(total)