# =============================================================================
#       COMPARACIÓN DE RENDIMIENTO: ENFOQUE ITERATIVO VS. RECURSIVO
# =============================================================================
#
# Este script mide y compara el tiempo de ejecución de las versiones
# iterativas y recursivas de los algoritmos de búsqueda para determinar
# cuál enfoque es más rápido en la práctica en Python.
#
# =============================================================================

import time
import random
import sys
from algoritmos import *

# Aumentamos el límite de recursión para las pruebas con listas grandes
sys.setrecursionlimit(20000)

def generar_lista(tamaño, ordenada=False):
    """
    Genera una lista de números. Si 'ordenada' es True, la devuelve ya ordenada.
    """
    lista = [random.randint(0, tamaño * 10) for _ in range(tamaño)]
    if ordenada:
        return sorted(lista)
    return lista

# --- 1. COMPARACIÓN DE BÚSQUEDA BINARIA ---
print(f"\n{'='*70}")
print("### 1. ANÁLISIS BÚSQUEDA BINARIA: Iterativa vs. Recursiva ###")
print(f"{'='*70}")
print("Ambas versiones requieren una lista ordenada. Mediremos su velocidad.")

tamaños_a_probar = [100, 1000, 5000]

for tamaño in tamaños_a_probar:
    print(f"\n--- Para una lista de {tamaño} elementos ---")
    lista_ordenada = generar_lista(tamaño, ordenada=True)
    objetivo = random.choice(lista_ordenada)

    # Medimos la versión Iterativa
    inicio_iter = time.time()
    busqueda_binaria_iterativa(lista_ordenada, objetivo)
    tiempo_iter = time.time() - inicio_iter
    print(f"  - ⏱️ Tiempo Versión Iterativa: {tiempo_iter:.6f} segundos")

    # Medimos la versión Recursiva
    inicio_rec = time.time()
    busqueda_binaria_recursiva(lista_ordenada, objetivo)
    tiempo_rec = time.time() - inicio_rec
    print(f"  - ⏱️ Tiempo Versión Recursiva: {tiempo_rec:.6f} segundos")
    
    # Veredicto
    if tiempo_iter < tiempo_rec:
        print("  --> Veredicto: La versión ITERATIVA fue más rápida.")
    else:
        print("  --> Veredicto: La versión RECURSIVA fue más rápida.")

# --- 2. COMPARACIÓN DE BÚSQUEDA LINEAL ---
print(f"\n\n{'='*70}")
print("### 2. ANÁLISIS BÚSQUEDA LINEAL: Iterativa vs. Recursiva ###")
print(f"{'='*70}")
print("Ambas versiones funcionan en listas desordenadas.")

for tamaño in tamaños_a_probar:
    print(f"\n--- Para una lista de {tamaño} elementos ---")
    lista_desordenada = generar_lista(tamaño)
    objetivo = random.choice(lista_desordenada)

    # Medimos la versión Iterativa (la estándar)
    inicio_iter_lin = time.time()
    busqueda_lineal(lista_desordenada, objetivo)
    tiempo_iter_lin = time.time() - inicio_iter_lin
    print(f"  - ⏱️ Tiempo Versión Iterativa: {tiempo_iter_lin:.6f} segundos")

    # Medimos la versión Recursiva
    inicio_rec_lin = time.time()
    busqueda_lineal_recursiva(lista_desordenada, objetivo)
    tiempo_rec_lin = time.time() - inicio_rec_lin
    print(f"  - ⏱️ Tiempo Versión Recursiva: {tiempo_rec_lin:.6f} segundos")

    # Veredicto
    if tiempo_iter_lin < tiempo_rec_lin:
        print("  --> Veredicto: La versión ITERATIVA fue más rápida.")
    else:
        print("  --> Veredicto: La versión RECURSIVA fue más rápida.")

