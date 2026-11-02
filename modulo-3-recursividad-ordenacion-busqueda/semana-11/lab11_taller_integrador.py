"""
Lab 11 — Taller Integrador: Ordenación + Búsqueda + Recursión
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Edward Hospina
Grupo: Lab B
Fecha: 02/11/2026

=============================================================
DECLARACIÓN DE USO DE IA (COMPLETAR ANTES DE ENTREGAR)
=============================================================
Herramienta usada      : DeepSeek (modelo de chat)
Para qué se usó        : Para comprender la lógica de la exponenciación rápida y cómo integrar los conceptos del módulo.
Qué hice yo            : Implementé todas las funciones, analicé las complejidades y resolví las preguntas de reflexión final.
Puedo explicar todo    : Sí
=============================================================

Este taller integra los tres grandes temas del Módulo 3. Deberás:
  - Elegir el algoritmo de ordenación más adecuado según el contexto.
  - Aplicar búsqueda binaria sobre la colección ordenada.
  - Diseñar una solución recursiva para un sub-problema.
  - Justificar las complejidades en las celdas marcadas como [ANÁLISIS].
"""

import time
import random


# =============================================================================
# PARTE 1: AGENDA DE CONTACTOS (ordenación + búsqueda)
# =============================================================================

CONTACTOS_EJEMPLO = [
    {"nombre": "Carlos", "apellido": "Zúñiga",   "telefono": "6001-0001"},
    {"nombre": "María",  "apellido": "Alvarado",  "telefono": "6001-0002"},
    {"nombre": "Luis",   "apellido": "Morales",   "telefono": "6001-0003"},
    {"nombre": "Ana",    "apellido": "Batista",   "telefono": "6001-0004"},
    {"nombre": "Pedro",  "apellido": "Rodríguez", "telefono": "6001-0005"},
    {"nombre": "Sandra", "apellido": "López",     "telefono": "6001-0006"},
    {"nombre": "Jorge",  "apellido": "Chávez",    "telefono": "6001-0007"},
    {"nombre": "Elena",  "apellido": "Morales",   "telefono": "6001-0008"},
]

def ordenar_contactos(contactos):
    """
    Ordena `contactos` por 'apellido' y, en caso de empate, por 'nombre'.
    Retorna UNA NUEVA lista ordenada.
    [ANÁLISIS]: Elegí el algoritmo de ordenación de Python (Timsort, O(n log n)) 
    porque es el más eficiente para datos reales. Si tuviera que implementarlo a mano, 
    usaría Merge Sort, ya que es estable (preserva el orden de los empates) y garantiza O(n log n).
    Complejidad: O(n log n).
    """
    # ============================================================
    # AGREGADO POR MÍ: usar sorted con tuplas para el doble criterio
    # Se hizo uso la herramienta de la inteligencia artificial DeepSeek 
    # como apoyo para comprender los conceptos.
    # ============================================================
    # Al usar (apellido, nombre) como clave, Python ordena primero por apellido
    # y si hay empate, usa el nombre.
    return sorted(contactos, key=lambda c: (c['apellido'], c['nombre']))
    # ============================================================


def buscar_por_apellido(contactos_ordenados, apellido_buscado):
    """
    Busca TODOS los contactos cuyo 'apellido' == apellido_buscado.
    Estrategia: Búsqueda binaria para encontrar uno, luego expandir a los lados.
    Complejidad esperada: O(log n + k) donde k = número de coincidencias.
    """
    # ============================================================
    # AGREGADO POR MÍ: búsqueda binaria y expansión
    # Se hizo uso la herramienta de la inteligencia artificial DeepSeek 
    # como apoyo para comprender los conceptos.
    # ============================================================
    izq = 0
    der = len(contactos_ordenados) - 1
    indice_encontrado = -1

    # 1. Búsqueda binaria para encontrar CUALQUIER coincidencia
    while izq <= der:
        mid = (izq + der) // 2
        apellido_actual = contactos_ordenados[mid]['apellido']
        
        if apellido_actual == apellido_buscado:
            indice_encontrado = mid
            break
        elif apellido_actual < apellido_buscado:
            izq = mid + 1
        else:
            der = mid - 1

    if indice_encontrado == -1:
        return []  # No se encontró ninguno

    # 2. Expandir hacia la izquierda y derecha
    resultado = [contactos_ordenados[indice_encontrado]]
    
    # Expandir izquierda
    i = indice_encontrado - 1
    while i >= 0 and contactos_ordenados[i]['apellido'] == apellido_buscado:
        resultado.insert(0, contactos_ordenados[i])
        i -= 1
        
    # Expandir derecha
    i = indice_encontrado + 1
    while i < len(contactos_ordenados) and contactos_ordenados[i]['apellido'] == apellido_buscado:
        resultado.append(contactos_ordenados[i])
        i += 1

    return resultado
    # ============================================================


# =============================================================================
# PARTE 2: ESTADÍSTICAS RECURSIVAS
# =============================================================================

def suma_recursiva(nums):
    """Calcula la suma de `nums` usando recursión. Complejidad: O(n)."""
    # ============================================================
    # AGREGADO POR MÍ:
    # Se hizo uso la herramienta de la inteligencia artificial DeepSeek 
    # como apoyo para comprender los conceptos.
    # ============================================================
    if not nums:  # Caso base
        return 0
    return nums[0] + suma_recursiva(nums[1:])
    # ============================================================


def maximo_recursivo(nums):
    """Encuentra el máximo de `nums` usando recursión. Complejidad: O(n)."""
    # ============================================================
    # AGREGADO POR MÍ:
    # Se hizo uso la herramienta de la inteligencia artificial DeepSeek 
    # como apoyo para comprender los conceptos.
    # ============================================================
    if len(nums) == 1:  # Caso base
        return nums[0]
    max_resto = maximo_recursivo(nums[1:])
    return nums[0] if nums[0] > max_resto else max_resto
    # ============================================================


def cuenta_mayores_recursivo(nums, umbral, i=0):
    """Cuenta cuántos elementos de nums[i:] son > umbral. Recursión de cola. O(n)."""
    # ============================================================
    # AGREGADO POR MÍ:
    # Se hizo uso la herramienta de la inteligencia artificial DeepSeek 
    # como apoyo para comprender los conceptos.
    # ============================================================
    if i == len(nums):  # Caso base
        return 0
    
    # Si el actual es mayor, suma 1 y sigue
    if nums[i] > umbral:
        return 1 + cuenta_mayores_recursivo(nums, umbral, i + 1)
    else:
        return cuenta_mayores_recursivo(nums, umbral, i + 1)
    # ============================================================


# =============================================================================
# PARTE 3: POTENCIAS Y EXPONENCIACIÓN RÁPIDA
# =============================================================================

def potencia_lenta(base, exp):
    """Calcula base^exp multiplicando una a una (O(n))."""
    if exp == 0:
        return 1
    return base * potencia_lenta(base, exp - 1)


def potencia_rapida(base, exp):
    """
    Calcula base^exp con exponenciación por cuadrado.
    Complejidad: O(log n).
    """
    if exp == 0:
        return 1
    # ============================================================
    # AGREGADO POR MÍ: casos par e impar
    # Se hizo uso la herramienta de la inteligencia artificial DeepSeek 
    # como apoyo para comprender los conceptos.
    # ============================================================
    if exp % 2 == 0:
        # base^exp = (base^(exp/2))^2
        mitad = potencia_rapida(base, exp // 2)
        return mitad * mitad
    else:
        # base^exp = base * base^(exp-1)
        return base * potencia_rapida(base, exp - 1)
    # ============================================================


# =============================================================================
# PARTE 4: PROBLEMA INTEGRADOR — TOP-K PRODUCTOS
# =============================================================================

CATALOGO = [
    {"nombre": "Audífonos BT",     "precio": 45.99},
    {"nombre": "Cargador USB-C",   "precio": 12.50},
    {"nombre": "Funda celular",    "precio": 8.99},
    {"nombre": "Teclado inalám.",  "precio": 35.00},
    {"nombre": "Mouse ergonómico", "precio": 28.75},
    {"nombre": "Webcam HD",        "precio": 55.00},
    {"nombre": "Hub USB 4 puertos","precio": 18.00},
    {"nombre": "Soporte laptop",   "precio": 22.50},
    {"nombre": "Cable HDMI 2m",    "precio": 9.99},
    {"nombre": "Parlante portátil","precio": 39.00},
]


def top_k_baratos(catalogo, k):
    """Retorna los k productos más baratos, ordenados de menor a mayor precio."""
    # ============================================================
    # AGREGADO POR MÍ:
    # Se hizo uso la herramienta de la inteligencia artificial DeepSeek 
    # como apoyo para comprender los conceptos.
    # ============================================================
    ordenados = sorted(catalogo, key=lambda p: p['precio'])
    return ordenados[:k]
    # ============================================================


def rango_precio(catalogo_ordenado, precio_min, precio_max):
    """
    Usando el catálogo YA ORDENADO por precio, retorna todos los
    productos cuyo precio está en [precio_min, precio_max].
    """
    # ============================================================
    # AGREGADO POR MÍ: usando búsqueda binaria (módulo bisect)
    # Se hizo uso la herramienta de la inteligencia artificial DeepSeek 
    # como apoyo para comprender los conceptos.
    # ============================================================
    import bisect
    
    # Extraemos solo los precios para hacer la búsqueda binaria
    precios = [p['precio'] for p in catalogo_ordenado]
    
    # Encontrar el índice del primer precio >= min
    izq = bisect.bisect_left(precios, precio_min)
    # Encontrar el índice del primer precio > max
    der = bisect.bisect_right(precios, precio_max)
    
    # Retornar la rebanada
    return catalogo_ordenado[izq:der]
    # ============================================================


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":
    # ---- PARTE 1 ----
    print("=" * 60)
    print("PARTE 1: Agenda de Contactos")
    print("=" * 60)

    ordenados = ordenar_contactos(CONTACTOS_EJEMPLO)
    if ordenados:
        print("Contactos ordenados:")
        for c in ordenados:
            print(f"  {c['apellido']:15} {c['nombre']:10} {c['telefono']}")

        encontrados = buscar_por_apellido(ordenados, "Morales")
        print(f"\nBúsqueda 'Morales': {len(encontrados) if encontrados else 0} resultado(s)")
        for c in (encontrados or []):
            print(f"  {c['nombre']} {c['apellido']} — {c['telefono']}")

        no_encontrado = buscar_por_apellido(ordenados, "García")
        print(f"Búsqueda 'García': {no_encontrado}")

    # ---- PARTE 2 ----
    print("\n" + "=" * 60)
    print("PARTE 2: Estadísticas Recursivas")
    print("=" * 60)
    nums = [4, 7, 2, 9, 1, 5]
    print(f"Lista: {nums}")
    print(f"  suma_recursiva:           {suma_recursiva(nums)}  (esperado: 28)")
    print(f"  maximo_recursivo:         {maximo_recursivo(nums)}  (esperado: 9)")
    print(f"  cuenta_mayores(umbral=4): {cuenta_mayores_recursivo(nums, 4)}  (esperado: 3)")
    print(f"  suma_recursiva([]):       {suma_recursiva([])}  (esperado: 0)")

    # ---- PARTE 3 ----
    print("\n" + "=" * 60)
    print("PARTE 3: Potencias")
    print("=" * 60)
    pares_prueba = [(2, 10), (3, 5), (5, 0), (7, 3)]
    for base, exp in pares_prueba:
        lenta = potencia_lenta(base, exp)
        rapida = potencia_rapida(base, exp)
        estado = "OK" if lenta == rapida else "ERROR"
        print(f"  [{estado}] {base}^{exp} = {lenta} (rápida={rapida})")

    print("\nComparación de tiempos (base=2, exp=1000):")
    t0 = time.perf_counter()
    for _ in range(10_000):
        potencia_lenta(2, 500)
    t_lenta = time.perf_counter() - t0

    t0 = time.perf_counter()
    for _ in range(10_000):
        potencia_rapida(2, 500)
    t_rapida = time.perf_counter() - t0

    print(f"  Lenta O(n):        {t_lenta:.4f}s")
    print(f"  Rápida O(log n):   {t_rapida:.4f}s")

    # ---- PARTE 4 ----
    print("\n" + "=" * 60)
    print("PARTE 4: Top-K Productos")
    print("=" * 60)
    baratos = top_k_baratos(CATALOGO, 3)
    print("Top-3 más baratos:")
    for p in (baratos or []):
        print(f"  {p['nombre']:25} ${p['precio']:.2f}")

    cat_ord = sorted(CATALOGO, key=lambda p: p['precio'])
    rango = rango_precio(cat_ord, 10.0, 30.0)
    print("\nProductos entre $10 y $30:")
    for p in (rango or []):
        print(f"  {p['nombre']:25} ${p['precio']:.2f}")

    # ---- REFLEXIÓN ----
    print("\n" + "=" * 60)
    print("REFLEXIÓN FINAL")
    print("=" * 60)
    print("""

[ANÁLISIS] 
1. ¿Qué algoritmo de ordenación elegiste en la Parte 1 y por qué?
   R: Usé la función sorted() de Python (Timsort). Es un algoritmo estable 
   (mantiene el orden de los nombres si hay apellidos iguales) y tiene 
   complejidad O(n log n), ideal para ordenar listas de diccionarios.

2. ¿Cuántas comparaciones haría la búsqueda binaria en una agenda
   de 1 000 contactos en el peor caso?
   R: Como la búsqueda binaria es O(log n), en el peor caso haría
   log2(1000) ≈ 10 comparaciones (ya que 2^10 = 1024).

3. ¿Cuántas llamadas recursivas hace potencia_rapida(2, 64)?
   R: Hace 7 llamadas. (64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1 -> 0).
   Al dividir el exponente a la mitad en cada paso, el número de 
   llamadas es log2(64) + 1.

Nota: En la prueba de tiempos, el exponente se redujo a 500 porque 
potencia_lenta excede el límite de recursión de Python (1000 llamadas) 
con exponentes más grandes. Esto demuestra en la práctica por qué O(n) 
es inviable para problemas grandes, mientras que O(log n) lo resuelve bien.
""")