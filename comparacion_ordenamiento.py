import time # Para medir el tiempo de ejecución de los algoritmos
import random # Para generar listas de números aleatorios
import sys # Para ajustar el límite de recursión en Python
from algoritmos import ordenamiento_burbuja, ordenamiento_rapido # funciones de ordenamiento

# Aumentamos el límite de recursión para que QuickSort no falle en listas grandes.
sys.setrecursionlimit(20000)

tamaños_a_probar = [100, 500, 1000, 2000]

print("--- Comparando Tiempos de Ordenamiento ---")

for tamaño in tamaños_a_probar:
    
    # Generamos una lista desordenada para cada prueba.
    lista_desordenada = [random.randint(0, tamaño) for _ in range(tamaño)]
    
    # Medimos el tiempo para Ordenamiento Burbuja.
    # Le pasamos una copia [:] para que no modifique la lista original.
    inicio_burbuja = time.time()
    ordenamiento_burbuja(lista_desordenada[:])
    tiempo_burbuja = time.time() - inicio_burbuja

    # Medimos el tiempo para Ordenamiento Rápido (QuickSort).
    inicio_rapido = time.time()
    ordenamiento_rapido(lista_desordenada[:])
    tiempo_rapido = time.time() - inicio_rapido
    
    # Imprimimos los resultados de esta ronda.
    print(f"\nLista de {tamaño} elementos:")
    print(f"  Burbuja:   {tiempo_burbuja:.4f} segundos")
    print(f"  QuickSort: {tiempo_rapido:.4f} segundos")

print("\n--- Fin de la comparación ---")