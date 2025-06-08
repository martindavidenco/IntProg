# =============================================================================
#           ANÁLISIS DE RENDIMIENTO DE ALGORITMOS DE BÚSQUEDA
# =============================================================================
#
# Este script realiza una comparación de rendimiento entre diferentes
# estrategias de búsqueda en una lista para responder a la pregunta:
# ¿Cuándo conviene ordenar una lista para usar búsqueda binaria,
# en lugar de usar una simple búsqueda lineal?
#
# =============================================================================

# 1. IMPORTACIONES
# -----------------
import time # Para medir el tiempo de ejecución de los algoritmos
import random # Para generar listas de números aleatorios
import sys # Para ajustar el límite de recursión en Python
from algoritmos import * # Importamos las funciones de búsqueda y ordenamiento definidas en algoritmos.py

# 2. CONFIGURACIÓN INICIAL
# -------------------------
sys.setrecursionlimit(20000)

# 3. FUNCIONES AUXILIARES
# -----------------------
def generar_lista(tamaño):
    """Genera una lista de números enteros aleatorios."""
    return [random.randint(0, tamaño * 10) for _ in range(tamaño)]

# 4. FLUJO PRINCIPAL DEL SCRIPT
# -----------------------------
if __name__ == "__main__":
    
    tamaños_a_probar = [100, 1000, 5000, 1000000]

    for tamaño in tamaños_a_probar:
        print(f"\n\n{'#'*60}")
        print(f"### ANÁLISIS PARA UNA LISTA DE {tamaño} ELEMENTOS ###")
        print(f"{'#'*60}")

        # Generamos una única lista desordenada y un objetivo para todas las pruebas de este tamaño.
        lista = generar_lista(tamaño)
        objetivo_a_buscar = random.choice(lista)

        # --- ESTRATEGIA 1: BÚSQUEDA LINEAL ---
        print("\n- ESTRATEGIA 1: Búsqueda Lineal (sin ordenar) ---")
        print("   Consiste en recorrer la lista desordenada elemento por elemento.")
        
        inicio_lineal = time.time()
        busqueda_lineal(lista, objetivo_a_buscar)
        costo_total_lineal = time.time() - inicio_lineal
        
        print(f"\n   COSTO TOTAL ESTRATEGIA 1: {costo_total_lineal:.6f} segundos")
        print("-" * 50)

        # --- ESTRATEGIA 2: ORDENAR + BÚSQUEDA BINARIA ---
        print("\n---  ESTRATEGIA 2: Ordenar y LUEGO Buscar ---")
        print("   Consiste en invertir tiempo en ordenar la lista para después usar la búsqueda binaria.")
        
        # Medimos el tiempo que tarda el ordenamiento
        inicio_ord = time.time()
        lista_ordenada = ordenamiento_rapido(lista) # Usamos el ordenamiento rápido
        tiempo_ordenamiento = time.time() - inicio_ord
        print(f"\n   Paso 1 (Ordenar con QuickSort): {tiempo_ordenamiento:.6f} segundos")

        # Medimos el tiempo que tarda la búsqueda binaria en la lista ya ordenada
        inicio_busq = time.time()
        busqueda_binaria_recursiva(lista_ordenada, objetivo_a_buscar)
        tiempo_busqueda = time.time() - inicio_busq
        print(f"   Paso 2 (Búsqueda Binaria):      {tiempo_busqueda:.6f} segundos")
        
        # Calculamos el costo total de esta estrategia (SUMA DE LOS 2 PASOS)
        costo_total_combinado = tiempo_ordenamiento + tiempo_busqueda
        
        print("   -------------------------------------------------")
        print(f"   COSTO TOTAL ESTRATEGIA 2: {costo_total_combinado:.6f} segundos")
        print("-" * 50)

        # --- VEREDICTO FINAL PARA ESTE TAMAÑO ---
        print("\n---  VEREDICTO ---")
        if costo_total_lineal < costo_total_combinado:
            print(f"   ¡La ESTRATEGIA 1 (Lineal) fue más rápida por {costo_total_combinado - costo_total_lineal:.6f} s!")
        else:
            print(f"   ¡La ESTRATEGIA 2 (Ordenar + Buscar) fue más rápida por {costo_total_lineal - costo_total_combinado:.6f} s!")