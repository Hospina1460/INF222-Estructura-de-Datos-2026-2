"""
Lab 12 — Árbol Binario y Recorridos
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Edward Hospina
Grupo: Lab B
Fecha: 21/11/2026

=============================================================
DECLARACIÓN DE USO DE IA (COMPLETAR ANTES DE ENTREGAR)
=============================================================
Herramienta usada      : DeepSeek (modelo de chat)
Para qué se usó        : Para comprender la lógica de los recorridos recursivos
                         (inorden, preorden, postorden), el recorrido por niveles
                         (BFS) con cola, y el cálculo de altura y conteo de nodos
                         en un árbol binario.
Qué hice yo            : Implementé todos los métodos, construí manualmente el árbol
                         de ejemplo, ejecuté y verifiqué los casos de prueba, y
                         comprendí por qué cada recorrido produce su salida esperada.
Puedo explicar todo    : Sí
=============================================================

Este laboratorio implementa un árbol binario con recorridos recursivos
y un recorrido por niveles (BFS) como tarea autónoma.
"""

from collections import deque  # para el recorrido por niveles (tarea)


class NodoArbol:
    """Nodo de un árbol binario."""

    def __init__(self, dato):
        self.dato = dato
        self.hijo_izq = None
        self.hijo_der = None

    def __str__(self):
        return str(self.dato)


class ArbolBinario:
    """
    Árbol binario con recorridos implementados de forma recursiva.
    La inserción es manual (no BST): el usuario construye el árbol
    asignando directamente hijo_izq e hijo_der a los nodos.
    """

    def __init__(self):
        self.raiz = None

    # ------------------------------------------------------------------
    # RECORRIDOS RECURSIVOS
    # ------------------------------------------------------------------

    def inorden(self, nodo=None, primera_llamada=True):
        """
        Recorrido inorden: izquierda → raíz → derecha.
        Retorna una lista con los datos en el orden visitado.
        """
        if primera_llamada:
            nodo = self.raiz
        # ============================================================
        # AGREGADO POR MÍ: implementación del recorrido inorden recursivo
        # Se hizo uso la herramienta de la inteligencia artificial DeepSeek
        # como apoyo para comprender los conceptos.
        # ============================================================
        if nodo is None:
            return []
        return (
            self.inorden(nodo.hijo_izq, False)
            + [nodo.dato]
            + self.inorden(nodo.hijo_der, False)
        )
        # ============================================================

    def preorden(self, nodo=None, primera_llamada=True):
        """
        Recorrido preorden: raíz → izquierda → derecha.
        Retorna una lista con los datos en el orden visitado.
        """
        if primera_llamada:
            nodo = self.raiz
        # ============================================================
        # AGREGADO POR MÍ: implementación del recorrido preorden recursivo
        # Se hizo uso la herramienta de la inteligencia artificial DeepSeek
        # como apoyo para comprender los conceptos.
        # ============================================================
        if nodo is None:
            return []
        return (
            [nodo.dato]
            + self.preorden(nodo.hijo_izq, False)
            + self.preorden(nodo.hijo_der, False)
        )
        # ============================================================

    def postorden(self, nodo=None, primera_llamada=True):
        """
        Recorrido postorden: izquierda → derecha → raíz.
        Retorna una lista con los datos en el orden visitado.
        """
        if primera_llamada:
            nodo = self.raiz
        # ============================================================
        # AGREGADO POR MÍ: implementación del recorrido postorden recursivo
        # Se hizo uso la herramienta de la inteligencia artificial DeepSeek
        # como apoyo para comprender los conceptos.
        # ============================================================
        if nodo is None:
            return []
        return (
            self.postorden(nodo.hijo_izq, False)
            + self.postorden(nodo.hijo_der, False)
            + [nodo.dato]
        )
        # ============================================================

    def por_niveles(self):
        """
        Recorrido por niveles (BFS): visita los nodos de arriba hacia abajo,
        izquierda a derecha dentro de cada nivel. Usa una cola.
        TAREA (trabajo autónomo): implementa este método.
        Retorna una lista con los datos en el orden visitado.
        """
        # ============================================================
        # AGREGADO POR MÍ: implementación del recorrido BFS con deque
        # Se hizo uso la herramienta de la inteligencia artificial DeepSeek
        # como apoyo para comprender los conceptos.
        # ============================================================
        if self.raiz is None:
            return []

        resultado = []
        cola = deque([self.raiz])

        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.dato)
            if nodo.hijo_izq is not None:
                cola.append(nodo.hijo_izq)
            if nodo.hijo_der is not None:
                cola.append(nodo.hijo_der)

        return resultado
        # ============================================================

    # ------------------------------------------------------------------
    # UTILIDADES
    # ------------------------------------------------------------------

    def altura(self, nodo=None, primera_llamada=True):
        """
        Retorna la altura del árbol (número de niveles - 1).
        Árbol vacío → -1. Solo la raíz → 0.
        """
        if primera_llamada:
            nodo = self.raiz
        # ============================================================
        # AGREGADO POR MÍ: cálculo recursivo de la altura del árbol
        # Se hizo uso la herramienta de la inteligencia artificial DeepSeek
        # como apoyo para comprender los conceptos.
        # ============================================================
        if nodo is None:
            return -1
        return 1 + max(
            self.altura(nodo.hijo_izq, False),
            self.altura(nodo.hijo_der, False)
        )
        # ============================================================

    def contar_nodos(self, nodo=None, primera_llamada=True):
        """Retorna el número de nodos en el árbol."""
        if primera_llamada:
            nodo = self.raiz
        # ============================================================
        # AGREGADO POR MÍ: conteo recursivo de nodos
        # Se hizo uso la herramienta de la inteligencia artificial DeepSeek
        # como apoyo para comprender los conceptos.
        # ============================================================
        if nodo is None:
            return 0
        return 1 + self.contar_nodos(nodo.hijo_izq, False) + self.contar_nodos(nodo.hijo_der, False)
        # ============================================================


# =============================================================================
# CONSTRUCCIÓN MANUAL DEL ÁRBOL DE EJEMPLO
# =============================================================================

def construir_arbol_ejemplo():
    """
    Construye el árbol:
            10
           /  \\
          5    20
         / \\     \\
        3   7    30
    """
    arbol = ArbolBinario()

    arbol.raiz = NodoArbol(10)

    arbol.raiz.hijo_izq = NodoArbol(5)
    arbol.raiz.hijo_der = NodoArbol(20)

    arbol.raiz.hijo_izq.hijo_izq = NodoArbol(3)
    arbol.raiz.hijo_izq.hijo_der = NodoArbol(7)
    arbol.raiz.hijo_der.hijo_der = NodoArbol(30)

    return arbol


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":
    arbol = construir_arbol_ejemplo()

    print("Árbol de ejemplo:")
    print("        10")
    print("       /  \\")
    print("      5    20")
    print("     / \\     \\")
    print("    3   7    30")
    print()

    inorden   = arbol.inorden()
    preorden  = arbol.preorden()
    postorden = arbol.postorden()
    niveles   = arbol.por_niveles()

    print(f"Inorden    (izq-raíz-der): {inorden}")
    print(f"  Esperado:                [3, 5, 7, 10, 20, 30]")
    print(f"  {'OK' if inorden == [3, 5, 7, 10, 20, 30] else 'ERROR'}")

    print(f"\nPreorden   (raíz-izq-der): {preorden}")
    print(f"  Esperado:                [10, 5, 3, 7, 20, 30]")
    print(f"  {'OK' if preorden == [10, 5, 3, 7, 20, 30] else 'ERROR'}")

    print(f"\nPostorden  (izq-der-raíz): {postorden}")
    print(f"  Esperado:                [3, 7, 5, 30, 20, 10]")
    print(f"  {'OK' if postorden == [3, 7, 5, 30, 20, 10] else 'ERROR'}")

    print(f"\nPor niveles (tarea):       {niveles}")
    print(f"  Esperado:                [10, 5, 20, 3, 7, 30]")
    print(f"  {'OK' if niveles == [10, 5, 20, 3, 7, 30] else 'ERROR'}")

    print(f"\nAltura del árbol: {arbol.altura()} (esperado: 2)")
    print(f"Número de nodos:  {arbol.contar_nodos()} (esperado: 6)")

    vacio = ArbolBinario()
    print(f"\nÁrbol vacío — altura: {vacio.altura()} (esperado: -1)")
    print(f"Árbol vacío — nodos:  {vacio.contar_nodos()} (esperado: 0)")
    print(f"Árbol vacío — inorden: {vacio.inorden()} (esperado: [])")