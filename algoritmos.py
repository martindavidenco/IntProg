# -----------------------------------------------------------------------------
#                           ALGORITMOS DE BÚSQUEDA
# -----------------------------------------------------------------------------

# Recorre la lista secuencialmente hasta encontrar el objetivo.
def busqueda_lineal(lista, objetivo):  # Revisa uno por uno, sin pre-requisitos.
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Versión recursiva de la búsqueda lineal, avanza índice por índice.
def busqueda_lineal_recursiva(lista, objetivo, indice=0):  # Se llama a sí misma para avanzar al siguiente.
    if indice >= len(lista):
        return -1
    if lista[indice] == objetivo:
        return indice
    return busqueda_lineal_recursiva(lista, objetivo, indice + 1)

# Búsqueda en lista ordenada que divide el espacio a la mitad con un bucle.
def busqueda_binaria_iterativa(lista, objetivo):  # 'Divide y vencerás' usando punteros (inicio, fin).
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Versión recursiva de la búsqueda binaria, se llama a sí misma en la mitad correcta.
def busqueda_binaria_recursiva(lista, objetivo, inicio=0, fin=None):  # 'Divide y vencerás' usando llamadas recursivas.
    if fin is None:
        fin = len(lista) - 1
    if inicio > fin:
        return -1
    medio = (inicio + fin) // 2
    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, fin)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, inicio, medio - 1)


# -----------------------------------------------------------------------------
#                          ALGORITMOS DE ORDENAMIENTO
# -----------------------------------------------------------------------------

# Ordena la lista comparando e intercambiando elementos adyacentes.
def ordenamiento_burbuja(lista):  # Compara cada elemento de la lista con el siguiente y los intercambia si están en el orden incorrecto.
    lista_copia = lista[:]
    n = len(lista_copia)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_copia[j] > lista_copia[j + 1]:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
    return lista_copia

# Elige un pivote y organiza todo en torno a él
def ordenamiento_rapido(lista):  # Divide la lista en dos partes y luego ordena cada parte de forma recursiva.
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    medios = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    
    return ordenamiento_rapido(menores) + medios + ordenamiento_rapido(mayores)