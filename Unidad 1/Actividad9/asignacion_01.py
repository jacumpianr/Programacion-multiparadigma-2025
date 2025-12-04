def crear_transformador(funcion):
    """
    Recibe una funcion y retorna otra funcion que aplica
    esa transformacion a cada elemento de una lista.
    """
    def transformador(lista):
        return [funcion(x) for x in lista]
    return transformador


def crear_filtro(predicado):
    """
    Recibe un predicado y retorna una funcion que filtra
    una lista dejando solo elementos que lo cumplen.
    """
    def filtrador(lista):
        return [x for x in lista if predicado(x)]
    return filtrador


def crear_reductor(funcion, valor_inicial):
    """
    Recibe una funcion de reduccion y un valor inicial
    retorna una funcion que reduce una lista a un solo valor.
    """
    def reductor(lista):
        acumulador = valor_inicial
        for x in lista:
            acumulador = funcion(acumulador, x)
        return acumulador
    return reductor


def componer(*funciones):
    """
    Recibe multiples funciones y retorna una nueva funcion
    que las aplica en secuencia (de izquierda a derecha).
    """
    def compuesto(lista):
        resultado = lista
        for funcion in funciones:
            resultado = funcion(resultado)
        return resultado
    return compuesto

numeros = [1, -2, 3, -4, 5, -6, 7, 8, -9, 10]

pipeline = componer(
    crear_filtro(lambda x: x > 0),
    crear_transformador(lambda x: x ** 2),
    crear_reductor(lambda acc, x: acc + x, 0)
)

resultado = pipeline(numeros)
print(f"Resultado: {resultado}") 