Proyecto Integrador: Programación I
Análisis comparativo de algoritmos de búsqueda y ordenamiento implementados en Python.

Integrantes:
Martin Davidenco - Comisión 12
Pablo Cozzi - Comisión 12
Tema del Proyecto:
Algoritmos de Búsqueda y Ordenamiento - Ventajas y desventajas de la búsqueda binaria

🎥 Video Explicativo: https://www.youtube.com/watch?v=0_SaU-NGsoQ

Objetivos:
Los objetivos principales de nuestro análisis fueron:

Implementar los algoritmos de búsqueda (Lineal y Binaria en versiones iterativas y recursivas) y de ordenamiento (Burbuja y QuickSort) como herramientas para nuestra investigación.
Demostrar teóricamente la eficiencia de la Búsqueda Binaria (O(
logn)) en datos ya ordenados, contando el número de operaciones en lugar de tiempo.
Evaluar el costo de rendimiento real que implica ordenar una lista antes de poder aplicar la Búsqueda Binaria, comparándolo con la simplicidad de una Búsqueda Lineal directa.
Responder a la pregunta central: ¿En qué escenarios conviene realmente utilizar cada estrategia de búsqueda?
Analizar como detalle técnico si el enfoque de implementación (iterativo vs. recursivo) tiene un impacto medible en el rendimiento.
Estructura del Proyecto:
El proyecto se compone de los siguientes archivos:

algoritmos.py: Nuestra librería principal. Contiene todas las funciones de búsqueda y ordenamiento.
analisis_teorico.py: Script que compara los algoritmos contando operaciones para demostrar la complejidad teórica (O(n) vs O(
logn)).
analisis_rendimiento.py: Script principal que mide el tiempo real y compara la estrategia "Búsqueda Lineal" vs. "Ordenar + Búsqueda Binaria".
comparacion_ordenamiento.py: Script que compara la eficiencia en tiempo de los dos algoritmos de ordenamiento implementados.
comparacion_recursividad.py: Script que compara el rendimiento de las implementaciones iterativas vs. las recursivas.
 Cómo Ejecutar los Análisis
Para ver los resultados de cada análisis, ejecuta los siguientes comandos en la terminal, asegurándote de estar en la carpeta del proyecto:


# Para ver la comparación teórica por operaciones
python analisis_teorico.py

# Para ver la comparación de estrategias por tiempo
python analisis_rendimiento.py

# Para comparar los algoritmos de ordenamiento
python comparacion_ordenamiento.py

# Para comparar las implementaciones recursivas vs iterativas
python comparacion_recursividad.py




