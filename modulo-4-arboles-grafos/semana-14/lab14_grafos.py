"""
Lab 14 — Grafos: representación, BFS y DFS
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Edward Hospina
Grupo: Lab B
Fecha: 21/11/2026

=============================================================
DECLARACIÓN DE USO DE IA (COMPLETAR ANTES DE ENTREGAR)
=============================================================
Herramienta usada      : DeepSeek (modelo de chat)
Para qué se usó        : Para comprender la lógica de los recorridos BFS (con cola)
                         y DFS (iterativo con pila y recursivo), y la reconstrucción
                         del camino más corto usando el mapa de predecesores.
Qué hice yo            : Implementé todos los métodos, ejecuté y verifiqué los
                         casos de prueba sobre el grafo de ejemplo y la red de
                         ciudades de Panamá, y comprobé que los recorridos y el
                         camino más corto producen los resultados esperados.
Puedo explicar todo    : Sí
=============================================================
"""

from collections import deque


class Grafo:
    """
    Grafo no dirigido representado con lista de adyacencia.
    Los vértices pueden ser cualquier valor hashable (entero, string, etc.).
    """

    def __init__(self):
        self._lista_adyacencia = {}  # {vértice: [vecinos]}

    def agregar_vertice(self, v):
        """Agrega el vértice v si no existe. O(1)."""
        if v not in self._lista_adyacencia:
            self._lista_adyacencia[v] = []

    def agregar_arista(self, v1, v2):
        """
        Agrega una arista NO DIRIGIDA entre v1 y v2.
        Agrega los vértices si no existen.
        O(1).
        """
        self.agregar_vertice(v1)
        self.agregar_vertice(v2)
        # ============================================================
        # AGREGADO POR MÍ: arista no dirigida (bidireccional)
        # Se hizo uso la herramienta de la inteligencia artificial DeepSeek
        # como apoyo para comprender los conceptos.
        # ============================================================
        self._lista_adyacencia[v1].append(v2)
        self._lista_adyacencia[v2].append(v1)
        # ============================================================

    def vecinos(self, v):
        """Retorna la lista de vecinos del vértice v."""
        return self._lista_adyacencia.get(v, [])

    def vertices(self):
        """Retorna la lista de todos los vértices."""
        return list(self._lista_adyacencia.keys())

    def __str__(self):
        """Representación legible de la lista de adyacencia."""
        lineas = []
        for v, vecinos in self._lista_adyacencia.items():
            lineas.append(f"  {v} → {vecinos}")
        return "Grafo:\n" + "\n".join(lineas)

    # ------------------------------------------------------------------
    # RECORRIDOS
    # ------------------------------------------------------------------

    def bfs(self, inicio):
        """
        Recorrido en anchura (Breadth-First Search) desde el vértice `inicio`.
        Usa una cola (deque).
        Retorna una lista con los vértices en el orden en que fueron visitados.
        """
        visitados = set()
        orden_visita = []
        cola = deque()

        # ============================================================
        # AGREGADO POR MÍ: implementación de BFS con cola
        # Se hizo uso la herramienta de la inteligencia artificial DeepSeek
        # como apoyo para comprender los conceptos.
        # ============================================================
        cola.append(inicio)
        visitados.add(inicio)

        while cola:
            v = cola.popleft()
            orden_visita.append(v)
            for vecino in self.vecinos(v):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        # ============================================================

        return orden_visita

    def dfs_iterativo(self, inicio):
        """
        Recorrido en profundidad (Depth-First Search) desde `inicio`.
        Versión iterativa: usa una pila (list de Python).
        Retorna la lista de vértices en orden de visita.
        """
        visitados = set()
        orden_visita = []
        pila = [inicio]

        # ============================================================
        # AGREGADO POR MÍ: implementación de DFS iterativo con pila
        # Se hizo uso la herramienta de la inteligencia artificial DeepSeek
        # como apoyo para comprender los conceptos.
        # ============================================================
        while pila:
            v = pila.pop()
            if v not in visitados:
                visitados.add(v)
                orden_visita.append(v)
                # Se apilan los vecinos en orden inverso para que el
                # primero de la lista se visite primero al hacer pop.
                for vecino in reversed(self.vecinos(v)):
                    if vecino not in visitados:
                        pila.append(vecino)
        # ============================================================

        return orden_visita

    def dfs_recursivo(self, inicio):
        """
        Recorrido en profundidad desde `inicio` usando recursividad.
        Retorna la lista de vértices en orden de visita.
        """
        visitados = set()
        orden_visita = []

        # ============================================================
        # AGREGADO POR MÍ: implementación de DFS recursivo
        # Se hizo uso la herramienta de la inteligencia artificial DeepSeek
        # como apoyo para comprender los conceptos.
        # ============================================================
        def _dfs(v):
            visitados.add(v)
            orden_visita.append(v)
            for vecino in self.vecinos(v):
                if vecino not in visitados:
                    _dfs(vecino)
        # ============================================================

        _dfs(inicio)
        return orden_visita

    def camino_bfs(self, inicio, fin):
        """
        Retorna el camino más corto (en número de aristas) de `inicio` a `fin`
        usando BFS. Retorna una lista de vértices que forman el camino,
        o None si no existe camino.
        """
        # ============================================================
        # AGREGADO POR MÍ: BFS con mapa de predecesores y reconstrucción
        # Se hizo uso la herramienta de la inteligencia artificial DeepSeek
        # como apoyo para comprender los conceptos.
        # ============================================================
        if inicio == fin:
            return [inicio]

        visitados = {inicio}
        predecesor = {inicio: None}
        cola = deque([inicio])

        while cola:
            v = cola.popleft()
            for vecino in self.vecinos(v):
                if vecino not in visitados:
                    visitados.add(vecino)
                    predecesor[vecino] = v
                    if vecino == fin:
                        # Reconstruir el camino desde fin hasta inicio
                        camino = []
                        actual = fin
                        while actual is not None:
                            camino.append(actual)
                            actual = predecesor[actual]
                        camino.reverse()
                        return camino
                    cola.append(vecino)

        return None  # no existe camino
        # ============================================================


# =============================================================================
# CONSTRUCCIÓN DE GRAFO DE EJEMPLO
# =============================================================================

def grafo_ejemplo_1():
    """
    Grafo:  A - B - D
            |   |
            C   E
    """
    g = Grafo()
    for arista in [("A","B"), ("A","C"), ("B","D"), ("B","E")]:
        g.agregar_arista(*arista)
    return g


def grafo_ciudades_panama():
    """
    Red simplificada de ciudades de Panamá conectadas por rutas.
    """
    g = Grafo()
    rutas = [
        ("Ciudad de Panamá", "La Chorrera"),
        ("Ciudad de Panamá", "Colón"),
        ("Ciudad de Panamá", "Chepo"),
        ("La Chorrera", "Arraiján"),
        ("La Chorrera", "Penonomé"),
        ("Penonomé", "Santiago"),
        ("Santiago", "Chitré"),
        ("Chitré", "Las Tablas"),
        ("Colón", "Portobelo"),
    ]
    for v1, v2 in rutas:
        g.agregar_arista(v1, v2)
    return g


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("Grafo de ejemplo 1")
    print("=" * 55)
    g1 = grafo_ejemplo_1()
    print(g1)

    print(f"\nBFS desde A:           {g1.bfs('A')}")
    print(f"DFS iterativo desde A: {g1.dfs_iterativo('A')}")
    print(f"DFS recursivo desde A: {g1.dfs_recursivo('A')}")

    print("\n" + "=" * 55)
    print("Red de ciudades de Panamá")
    print("=" * 55)
    g2 = grafo_ciudades_panama()
    print(g2)

    inicio = "Ciudad de Panamá"
    print(f"\nBFS desde '{inicio}':")
    for v in g2.bfs(inicio):
        print(f"  {v}")

    print(f"\nCamino más corto de 'Ciudad de Panamá' a 'Las Tablas':")
    camino = g2.camino_bfs("Ciudad de Panamá", "Las Tablas")
    if camino:
        print("  " + " → ".join(camino))
    else:
        print("  No existe camino")