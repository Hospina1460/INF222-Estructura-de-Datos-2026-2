"""
Lab 8 — Recursividad (con uso declarado de IA)
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Edward Hospina
Grupo: Lab B
Fecha: 02/11/2026

=============================================================
DECLARACIÓN DE USO DE IA (COMPLETAR ANTES DE ENTREGAR)
=============================================================
Herramienta usada      : DeepSeek (modelo de chat)
Para qué se usó        : Para obtener el trazado paso a paso de fibonacci(5) y comprender cómo funciona la pila de llamadas.
Qué hice yo            : Implementé todas las funciones del laboratorio, analicé la lógica y reescribí el trazado con mis propias palabras, además dibujé el diagrama ASCII de la pila.
Puedo explicar todo    : Sí
=============================================================
"""

import time
from functools import lru_cache


# =============================================================================
# PARTE 1 — FACTORIAL
# =============================================================================

def factorial(n):
    """
    Calcula n! de forma recursiva.
    Caso base: factorial(0) = 1
    Caso recursivo: factorial(n) = n × factorial(n-1)
    Complejidad: O(n) tiempo, O(n) espacio (por la pila de llamadas).
    """
    # ============================================================
    # AGREGADO POR MÍ: implementación recursiva
    # ============================================================
    if n == 0:          # Caso base
        return 1
    return n * factorial(n - 1)  # Caso recursivo
    # ============================================================


# =============================================================================
# PARTE 2 — FIBONACCI
# =============================================================================

def fibonacci_recursivo(n):
    """
    Calcula el n-ésimo número de Fibonacci recursivamente.
    ⚠️  Esta implementación es ineficiente: O(2^n) llamadas.
    Solo para propósitos de análisis y trazado.
    """
    # ============================================================
    # AGREGADO POR MÍ: implementación recursiva (ingenua)
    # ============================================================
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
    # ============================================================


@lru_cache(maxsize=None)
def fibonacci_memoizado(n):
    """
    Calcula el n-ésimo número de Fibonacci con memoización.
    O(n) tiempo, O(n) espacio.
    """
    # ============================================================
    # AGREGADO POR MÍ: implementación recursiva con memoización
    # ============================================================
    if n <= 1:
        return n
    return fibonacci_memoizado(n - 1) + fibonacci_memoizado(n - 2)
    # ============================================================


def fibonacci_iterativo(n):
    """
    Calcula el n-ésimo número de Fibonacci iterativamente.
    O(n) tiempo, O(1) espacio.
    """
    # ============================================================
    # AGREGADO POR MÍ: implementación iterativa
    # ============================================================
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
    # ============================================================


# =============================================================================
# PARTE 3 — TORRES DE HANOI
# =============================================================================

movimientos = []  # lista global para registrar los movimientos

def torres_de_hanoi(n, origen, destino, auxiliar):
    """
    Resuelve el problema de Torres de Hanoi para n discos.
    Complejidad: O(2^n - 1) movimientos.
    """
    # ============================================================
    # AGREGADO POR MÍ: implementación recursiva
    # ============================================================
    if n == 1:
        movimientos.append(f"Mover disco 1 de {origen} a {destino}")
        return
    
    # 1. Mover n-1 discos de origen a auxiliar
    torres_de_hanoi(n - 1, origen, auxiliar, destino)
    
    # 2. Mover el disco más grande de origen a destino
    movimientos.append(f"Mover disco {n} de {origen} a {destino}")
    
    # 3. Mover n-1 discos de auxiliar a destino
    torres_de_hanoi(n - 1, auxiliar, destino, origen)
    # ============================================================


# =============================================================================
# PARTE 4 — TRAZADO CON IA (obligatorio)
# =============================================================================
"""
INSTRUCCIONES:
1. Ejecuta fibonacci_recursivo(5) en tu mente o en papel primero.
2. Luego consulta un asistente de IA con este prompt:
   "Muéstrame el trazado paso a paso de la pila de llamadas de fibonacci(5)
    usando la versión recursiva simple (sin memoización). Usa indentación para
    mostrar la jerarquía de llamadas."
3. Copia el trazado que generó la IA en el espacio de abajo.
4. Reescríbelo CON TUS PROPIAS PALABRAS en el espacio "Trazado propio".
   Dibuja también el diagrama ASCII de la pila de llamadas.

TRAZADO GENERADO POR IA:
Llamada inicial: fibonacci_recursivo(5)

fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1) → Caso base, retorna 1
│   │   │   └── fib(0) → Caso base, retorna 0
│   │   │   [Suma 1 + 0] → fib(2) retorna 1
│   │   └── fib(1) → Caso base, retorna 1
│   │   [Suma 1 + 1] → fib(3) retorna 2
│   └── fib(2)
│       ├── fib(1) → Caso base, retorna 1
│       └── fib(0) → Caso base, retorna 0
│       [Suma 1 + 0] → fib(2) retorna 1
│   [Suma 2 + 1] → fib(4) retorna 3
└── fib(3)
    ├── fib(2)
    │   ├── fib(1) → Caso base, retorna 1
    │   └── fib(0) → Caso base, retorna 0
    │   [Suma 1 + 0] → fib(2) retorna 1
    └── fib(1) → Caso base, retorna 1
    [Suma 1 + 1] → fib(3) retorna 2
[Suma 3 + 2] → fib(5) retorna 5

Nota sobre la pila (call stack): 
La pila se va llenando hacia abajo en la primera rama izquierda (5→4→3→2→1). 
Al llegar al caso base fib(1), la función retorna y se "desapila" para calcular 
fib(0), luego se desapila fib(2) devolviendo 1, y así sucesivamente. Al final, 
las dos grandes ramas (fib(4) y fib(3)) se suman en el nivel superior para dar 5.


TRAZADO PROPIO (reescrito por el estudiante, sin copiar de la IA):

Para calcular fib(5), la función no lo hace de un solo golpe. Primero pide 
calcular fib(4) y fib(3). 

Entonces para sacar el fib(4), vuelve a pedir el fib(3) y el fib(2). 
Y para sacar ese fib(3), vuelve a pedir el fib(2) y el fib(1). 

Es un proceso en el que si quiero resolver un número grande, tengo que resolver los dos anteriores, 
y esos a su vez piden resolver más anteriores.

La función se sigue llamando a sí misma y bajando hasta que choca con el 
límite: cuando llega a fib(1) o fib(0), se frena y 
devuelve un número simple. Ahí empieza a devolverse todo hacia atrás, sumando 
los numeritos hasta que por fin llega arriba y me da el resultado final (que es 5).

Lo malo en esto es que hace muchísimo trabajo repetido. Por ejemplo, calcula fib(2) 
varias veces en diferentes ramas, y eso lo vuelve súper lento (ineficiente).

DIAGRAMA ASCII DE LA PILA DE LLAMADAS (dibujado por ti):

               fib(5)
             /        \
        fib(4)          fib(3)
       /      \        /      \
   fib(3)   fib(2)  fib(2)  fib(1)
   /    \    /  \    /  \
fib(2) fib(1) 1  0   1   0
 /  \
1    0

(Este es el árbol de llamadas. La "pila" en memoria se llena verticalmente por 
la rama izquierda primero: fib(5) -> fib(4) -> fib(3) -> fib(2) -> fib(1). 
Al llegar al caso base, se desapila retornando los valores).
"""


# =============================================================================
# CASOS DE PRUEBA Y COMPARACIÓN DE TIEMPOS
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("PARTE 1 — Factorial")
    print("=" * 55)
    for n in [0, 1, 5, 10]:
        print(f"  factorial({n}) = {factorial(n)}")

    print("\n" + "=" * 55)
    print("PARTE 2 — Fibonacci: comparación de eficiencia")
    print("=" * 55)
    casos = [10, 20, 30, 35]
    for n in casos:
        t0 = time.perf_counter()
        r = fibonacci_recursivo(n)
        t_rec = time.perf_counter() - t0

        t0 = time.perf_counter()
        m = fibonacci_memoizado(n)
        t_mem = time.perf_counter() - t0

        t0 = time.perf_counter()
        i = fibonacci_iterativo(n)
        t_it = time.perf_counter() - t0

        assert r == m == i, f"Discrepancia en fib({n}): {r}, {m}, {i}"
        print(f"  fib({n:2d}) = {r:10d} | recursivo: {t_rec:.4f}s | memo: {t_mem:.6f}s | iter: {t_it:.6f}s")

    print("\n" + "=" * 55)
    print("PARTE 3 — Torres de Hanoi (n=3)")
    print("=" * 55)
    movimientos.clear()
    torres_de_hanoi(3, "A", "C", "B")
    print(f"  Total de movimientos para n=3: {len(movimientos)} (esperado: 7)")
    for mov in movimientos:
        print(f"  {mov}")

    print(f"\n  Para n=10: {2**10 - 1} movimientos (2^10 - 1)")
    print(f"  Para n=20: {2**20 - 1:,} movimientos — ¿ves por qué O(2^n) escala mal?")