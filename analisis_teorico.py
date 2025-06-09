# =============================================================================
#           ANÁLISIS TEÓRICO DE ALGORITMOS DE BÚSQUEDA
# =============================================================================
#
# Este script asume que la lista YA ESTÁ ORDENADA de antemano y compara
# el número de operaciones (comparaciones) de cada algoritmo de búsqueda
# para demostrar su complejidad teórica.
#
# =============================================================================

import random
import math # La usaremos para calcular el logaritmo

# 1. FUNCIONES DE BÚSQUEDA CON CONTADOR DE COMPARACIONES

def busqueda_lineal_con_contador(lista, objetivo):
    """
    Busca un elemento y cuenta cuántas comparaciones realiza.
    """
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones += 1 # Cada vez que revisa un elemento, es una comparación
        if lista[i] == objetivo:
            return (i, comparaciones)
    return (-1, comparaciones)

def busqueda_binaria_con_contador(lista, objetivo):
    """
    Busca un elemento en una lista ordenada y cuenta las comparaciones.
    """
    comparaciones = 0
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        comparaciones += 1 # Cada vez que entra al bucle, hace una comparación
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return (medio, comparaciones)
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return (-1, comparaciones)

# 2. FLUJO PRINCIPAL DEL ANÁLISIS TEÓRICO
# ----------------------------------------
# (Todo el código de aquí en adelante fue movido un nivel a la izquierda)

tamaños_a_probar = [10, 100, 1000, 10000, 100000]

# Imprimimos la cabecera de nuestra tabla de resultados
print(f"{'='*67}")
print(f"| {'Tamaño Lista':<15} | {'B. Lineal (Op.)':<20} | {'B. Binaria (Op.)':<20} |")
print(f"|{'-'*17}|{'-'*22}|{'-'*22}|")

for tamaño in tamaños_a_probar:
    # Generamos una lista QUE YA ESTÁ ORDENADA
    lista_ordenada = sorted([random.randint(0, tamaño * 10) for _ in range(tamaño)])
    objetivo = random.choice(lista_ordenada) # Elegimos un objetivo que sabemos que existe

    # Ejecutamos las búsquedas y obtenemos el número de operaciones
    _, ops_lineal = busqueda_lineal_con_contador(lista_ordenada, objetivo)
    _, ops_binaria = busqueda_binaria_con_contador(lista_ordenada, objetivo)

    # Imprimimos una fila de la tabla con los resultados
    print(f"| {tamaño:<15,d} | {ops_lineal:<20,d} | {ops_binaria:<20,d} |")

print(f"{'='*67}")

print("\nConclusiones del Análisis Teórico:")
print("1. El número de operaciones de la Búsqueda Lineal crece de forma directamente proporcional al tamaño de la lista (O(n)).")
print("2. El número de operaciones de la Búsqueda Binaria crece de forma logarítmica, es decir, muy lentamente (O(log n)).")
