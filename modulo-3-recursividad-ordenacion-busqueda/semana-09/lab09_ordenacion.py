"""
Lab 9 — Algoritmos de Ordenación y Comparación de Eficiencia
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Edward Hospina
Grupo: Lab B
Fecha: 09/11/2026

DECLARACIÓN DE USO DE IA:
He utilizado la herramienta de inteligencia artificial DeepSeek como apoyo
para estructurar la lógica de los algoritmos de ordenación.
"""

import time
import random


# =============================================================================
# ALGORITMOS DE ORDENACIÓN
# =============================================================================

def burbuja(arr):
    """
    Ordena arr de menor a mayor usando bubble sort.
    Optimización: si en una pasada no hubo intercambios, el arreglo ya está ordenado.
    Retorna la lista ordenada (copia, no modifica el original).
    Complejidad: O(n) mejor caso (con flag), O(n²) promedio y peor caso.
    """
    lista = list(arr)  # trabaja sobre copia
    n = len(lista)
    # ============================================================
    # AGREGADO POR MÍ: implementación de Burbuja con flag
    # Se hizo uso la herramienta de la inteligencia artificial DeepSeek como apoyo para comprender los conceptos.
    # ============================================================
    for i in range(n):
        intercambiado = False
        # El -i es porque los últimos i elementos ya están ordenados
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        if not intercambiado:  # Optimización
            break
    # ============================================================
    return lista


def seleccion(arr):
    """
    Ordena arr de menor a mayor usando selection sort.
    En cada iteración, encuentra el mínimo del resto y lo lleva a su posición.
    Retorna la lista ordenada (copia).
    Complejidad: O(n²) en todos los casos.
    """
    lista = list(arr)
    n = len(lista)
    # ============================================================
    # AGREGADO POR MÍ: implementación de Selección
    # Se hizo uso la herramienta de la inteligencia artificial DeepSeek como apoyo para comprender los conceptos.
    # ============================================================
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        # Intercambiar el mínimo encontrado con la posición actual
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    # ============================================================
    return lista


def insercion(arr):
    """
    Ordena arr de menor a mayor usando insertion sort.
    Eficiente para arreglos pequeños o casi ordenados.
    Retorna la lista ordenada (copia).
    Complejidad: O(n) mejor caso (casi ordenado), O(n²) promedio y peor caso.
    """
    lista = list(arr)
    # ============================================================
    # AGREGADO POR MÍ: implementación de Inserción
    # Se hizo uso la herramienta de la inteligencia artificial DeepSeek como apoyo para comprender los conceptos.
    # ============================================================
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        # Mover los elementos mayores que la clave una posición adelante
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    # ============================================================
    return lista


# =============================================================================
# AMPLIACIÓN OPCIONAL: merge sort (O(n log n))
# =============================================================================

def merge_sort(arr):
    """
    Ordena arr usando merge sort (dividir y vencer).
    Retorna una nueva lista ordenada.
    Complejidad: O(n log n) en todos los casos. No es in situ.
    """
    # ============================================================
    # AGREGADO POR MÍ: implementación de Merge Sort (ampliación)
    # Se hizo uso la herramienta de la inteligencia artificial DeepSeek como apoyo para comprender los conceptos.
    # ============================================================
    if len(arr) <= 1:
        return list(arr)
    
    medio = len(arr) // 2
    izquierda = merge_sort(arr[:medio])
    derecha = merge_sort(arr[medio:])
    
    return _mezclar(izquierda, derecha)

def _mezclar(izq, der):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado
    # ============================================================


# =============================================================================
# GENERADORES DE ARREGLOS DE PRUEBA
# =============================================================================

def arreglo_aleatorio(n, minval=1, maxval=10_000):
    return [random.randint(minval, maxval) for _ in range(n)]

def arreglo_ordenado(n):
    return list(range(1, n + 1))

def arreglo_invertido(n):
    return list(range(n, 0, -1))

def arreglo_casi_ordenado(n, swaps=5):
    arr = list(range(1, n + 1))
    for _ in range(swaps):
        i, j = random.sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


# =============================================================================
# FUNCIÓN DE MEDICIÓN
# =============================================================================

def medir_tiempo(algoritmo, arr):
    """Ejecuta `algoritmo(arr)` y retorna (resultado, segundos)."""
    t0 = time.perf_counter()
    resultado = algoritmo(arr)
    t1 = time.perf_counter()
    return resultado, t1 - t0


# =============================================================================
# VERIFICACIÓN DE CORRECTITUD
# =============================================================================

def verificar_todos(casos_prueba):
    """Verifica que los tres algoritmos producen el mismo resultado que sorted()."""
    print("Verificando correctitud...")
    for desc, arr in casos_prueba:
        esperado = sorted(arr)
        for nombre, func in [("burbuja", burbuja), ("seleccion", seleccion), ("insercion", insercion)]:
            resultado = func(arr)
            ok = resultado == esperado
            print(f"  [{('OK' if ok else 'ERROR')}] {nombre:10s} en '{desc}'")
            if not ok:
                print(f"       esperado: {esperado[:10]}...")
                print(f"       obtenido: {resultado[:10]}...")


# =============================================================================
# EXPERIMENTO PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    random.seed(42)

    # Verificación con arreglos pequeños
    casos_prueba = [
        ("vacío", []),
        ("un elemento", [5]),
        ("ya ordenado", [1, 2, 3, 4, 5]),
        ("invertido", [5, 4, 3, 2, 1]),
        ("aleatorio", [3, 1, 4, 1, 5, 9, 2, 6]),
    ]
    verificar_todos(casos_prueba)

    print("\n" + "=" * 65)
    print("Comparación de tiempos (en segundos)")
    print("=" * 65)

    tamanios = [100, 1_000, 5_000, 10_000]
    tipos = [
        ("aleatorio", arreglo_aleatorio),
        ("ordenado",  arreglo_ordenado),
        ("invertido", arreglo_invertido),
    ]

    encabezado = f"{'N':>7} | {'tipo':>10} | {'burbuja':>10} | {'seleccion':>10} | {'insercion':>10}"
    print(encabezado)
    print("-" * len(encabezado))

    for n in tamanios:
        for desc, generador in tipos:
            arr = generador(n)
            _, t_burbuja   = medir_tiempo(burbuja,   arr)
            _, t_seleccion = medir_tiempo(seleccion, arr)
            _, t_insercion = medir_tiempo(insercion, arr)
            print(f"{n:>7,} | {desc:>10} | {t_burbuja:>10.4f} | {t_seleccion:>10.4f} | {t_insercion:>10.4f}")

    print("\n¿Qué observas? Escribe tus conclusiones aquí:")
    # ============================================================
    # AGREGADO POR MÍ: conclusiones del experimento
    # Se hizo uso la herramienta de la inteligencia artificial DeepSeek como apoyo para comprender los conceptos.
    # ============================================================
    print("  1. El algoritmo de Inserción es el más rápido cuando el arreglo ya está ordenado (O(n)), ya que solo hace una pasada.")
    print("  2. Burbuja y Selección son muy lentos (O(n²)) para arreglos grandes o invertidos, notándose una gran diferencia de tiempo en 10,000 elementos.")
    print("  3. La optimización con flag en Burbuja ayuda mucho en el mejor caso (arreglos ordenados), pero no salva su rendimiento en el peor caso.")
    # ============================================================