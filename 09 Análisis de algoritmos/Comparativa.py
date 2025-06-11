import time
# Búsqueda lineal
def busqueda_lineal(lista, objetivo):
    for i, valor in enumerate(lista):
        if valor == objetivo:
            return i
    return -1
# Búsqueda binaria
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
# Llamadas a las funciones para diferentes tamaños
for n in [100, 1000, 10000, 1000000]:
    lista = list(range(n))
    objetivo = n - 1
    inicio = time.time()
    busqueda_lineal(lista, objetivo)
    fin = time.time()
    print(f"Lineal - Tamaño {n}: {fin - inicio:.6f} segundos")
    inicio = time.time()
    busqueda_binaria(lista, objetivo)
    fin = time.time()
    print(f"Binaria - Tamaño {n}: {fin - inicio:.6f} segundos")