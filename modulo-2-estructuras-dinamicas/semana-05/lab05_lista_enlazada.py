"""
Lab 5 — Lista Enlazada Simple
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Edward Hospina
Grupo: Lab B
Fecha: 18/10/2026

DECLARACIÓN DE USO DE IA:
He utilizado la herramienta de inteligencia artificial DeepSeek como apoyo
para comprender los conceptos y estructurar la lógica del laboratorio.
"""


class Nodo:
    """Nodo de una lista enlazada simple."""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    """
    Lista enlazada simple con referencia a la cabeza.
    Los nodos NO son accesibles directamente desde el exterior;
    toda operación se hace a través de los métodos de esta clase.
    """

    def __init__(self):
        self._cabeza = None
        self._tamanio = 0

    # ------------------------------------------------------------------
    # INSERCIÓN
    # ------------------------------------------------------------------

    def insertar_inicio(self, dato):
        """Inserta dato al inicio de la lista. O(1)."""
        # ============================================================
        # SE AGREGÓ ESTA PARTE AL CÓDIGO DADO POR EL PROFESOR: Se hizo uso la herramienta 
        # de inteligencia artificial DeepSeek como apoyo para comprender los conceptos.
        # ============================================================
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self._cabeza
        self._cabeza = nuevo_nodo
        self._tamanio += 1
        # ============================================================

    def insertar_final(self, dato):
        """Inserta dato al final de la lista. O(n)."""
        # ============================================================
        # SE AGREGÓ ESTA PARTE AL CÓDIGO DADO POR EL PROFESOR: Se hizo uso la herramienta 
        # de inteligencia artificial DeepSeek como apoyo para comprender los conceptos.
        # ============================================================
        nuevo_nodo = Nodo(dato)
        if self.es_vacia():
            self._cabeza = nuevo_nodo
        else:
            actual = self._cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self._tamanio += 1
        # ============================================================

    def insertar_en_posicion(self, posicion, dato):
        """
        Inserta dato en la posición indicada (0-indexed).
        posición 0 equivale a insertar_inicio.
        Si posición >= tamaño, inserta al final.
        O(n).
        """
        # ============================================================
        # SE AGREGÓ ESTA PARTE AL CÓDIGO DADO POR EL PROFESOR: Se hizo uso la herramienta 
        # de inteligencia artificial DeepSeek como apoyo para comprender los conceptos.
        # ============================================================
        if posicion <= 0:
            self.insertar_inicio(dato)
            return
        if posicion >= self._tamanio:
            self.insertar_final(dato)
            return

        nuevo_nodo = Nodo(dato)
        actual = self._cabeza
        # Avanzar hasta el nodo ANTERIOR a la posición
        for _ in range(posicion - 1):
            actual = actual.siguiente
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo
        self._tamanio += 1
        # ============================================================

    # ------------------------------------------------------------------
    # ELIMINACIÓN
    # ------------------------------------------------------------------

    def eliminar(self, dato):
        """
        Elimina la primera ocurrencia de dato en la lista.
        Retorna True si se encontró y eliminó, False si no existe.
        Casos borde: eliminar la cabeza, eliminar un nodo intermedio,
                     eliminar el único nodo, dato no existe.
        O(n).
        """
        # ============================================================
        # SE AGREGÓ ESTA PARTE AL CÓDIGO DADO POR EL PROFESOR: Se hizo uso la herramienta 
        # de inteligencia artificial DeepSeek como apoyo para comprender los conceptos.
        # ============================================================
        # Caso 1: lista vacía
        if self.es_vacia():
            return False

        # Caso 2: el dato está en la cabeza
        if self._cabeza.dato == dato:
            self._cabeza = self._cabeza.siguiente
            self._tamanio -= 1
            return True

        # Caso 3: el dato está en el medio o al final
        anterior = self._cabeza
        actual = self._cabeza.siguiente
        while actual is not None:
            if actual.dato == dato:
                anterior.siguiente = actual.siguiente
                self._tamanio -= 1
                return True
            anterior = actual
            actual = actual.siguiente

        # Caso 4: no existe
        return False
        # ============================================================

    def eliminar_en_posicion(self, posicion):
        """
        Elimina el nodo en la posición indicada (0-indexed).
        Lanza IndexError si la posición está fuera de rango.
        O(n).
        """
        # ============================================================
        # SE AGREGÓ ESTA PARTE AL CÓDIGO DADO POR EL PROFESOR: Se hizo uso la herramienta 
        # de inteligencia artificial DeepSeek como apoyo para comprender los conceptos.
        # ============================================================
        if posicion < 0 or posicion >= self._tamanio:
            raise IndexError("Posición fuera de rango")

        # Caso 1: eliminar la cabeza
        if posicion == 0:
            dato = self._cabeza.dato
            self._cabeza = self._cabeza.siguiente
            self._tamanio -= 1
            return dato

        # Caso 2: eliminar en medio o al final
        anterior = self._cabeza
        for _ in range(posicion - 1):
            anterior = anterior.siguiente
        actual = anterior.siguiente
        dato = actual.dato
        anterior.siguiente = actual.siguiente
        self._tamanio -= 1
        return dato
        # ============================================================

    # ------------------------------------------------------------------
    # BÚSQUEDA Y ACCESO
    # ------------------------------------------------------------------

    def buscar(self, dato):
        """
        Retorna True si dato está en la lista, False si no.
        O(n).
        """
        # ============================================================
        # SE AGREGÓ ESTA PARTE AL CÓDIGO DADO POR EL PROFESOR: Se hizo uso la herramienta 
        # de inteligencia artificial DeepSeek como apoyo para comprender los conceptos.
        # ============================================================
        actual = self._cabeza
        while actual is not None:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False
        # ============================================================

    def obtener(self, indice):
        """
        Retorna el dato en la posición `indice` (0-indexed).
        Lanza IndexError si el índice está fuera de rango.
        O(n).
        """
        # ============================================================
        # SE AGREGÓ ESTA PARTE AL CÓDIGO DADO POR EL PROFESOR: Se hizo uso la herramienta 
        # de inteligencia artificial DeepSeek como apoyo para comprender los conceptos.
        # ============================================================
        if indice < 0 or indice >= self._tamanio:
            raise IndexError("Índice fuera de rango")
        actual = self._cabeza
        for _ in range(indice):
            actual = actual.siguiente
        return actual.dato
        # ============================================================

    # ------------------------------------------------------------------
    # OTROS
    # ------------------------------------------------------------------

    def invertir(self):
        """
        Invierte la lista in situ (sin crear nuevos nodos, solo re-enlaza).
        O(n).
        Ejemplo: [1→2→3] queda como [3→2→1]
        """
        # ============================================================
        # SE AGREGÓ ESTA PARTE AL CÓDIGO DADO POR EL PROFESOR: Se hizo uso la herramienta 
        # de inteligencia artificial DeepSeek como apoyo para comprender los conceptos.
        # ============================================================
        anterior = None
        actual = self._cabeza
        while actual is not None:
            siguiente = actual.siguiente   # guardar el siguiente
            actual.siguiente = anterior    # invertir el enlace
            anterior = actual              # avanzar anterior
            actual = siguiente             # avanzar actual
        self._cabeza = anterior
        # ============================================================

    def tamanio(self):
        """Retorna el número de elementos. O(1)."""
        return self._tamanio

    def es_vacia(self):
        """Retorna True si la lista no tiene elementos."""
        return self._cabeza is None

    def __str__(self):
        """Representación: cabeza → [1] → [2] → [3] → None"""
        nodos = []
        actual = self._cabeza
        while actual is not None:
            nodos.append(str(actual.dato))
            actual = actual.siguiente
        return "cabeza → " + " → ".join(nodos) + " → None"

    def __len__(self):
        return self._tamanio


# =============================================================================
# COMPARACIÓN EMPÍRICA DE TIEMPOS
# =============================================================================

def comparar_tiempos_insercion_inicio(n=10_000):
    """
    Compara el tiempo de insertar n elementos al inicio:
    - Lista de Python (insert(0, dato)) → O(n) por operación → O(n²) total
    - ListaEnlazada (insertar_inicio(dato)) → O(1) por operación → O(n) total
    """
    # ============================================================
    # SE AGREGÓ ESTA PARTE AL CÓDIGO DADO POR EL PROFESOR: Se hizo uso la herramienta 
    # de inteligencia artificial DeepSeek como apoyo para comprender los conceptos.
    # ============================================================
    import time

    # Lista de Python
    lista_python = []
    t0 = time.perf_counter()
    for i in range(n):
        lista_python.insert(0, i)
    t1 = time.perf_counter()
    tiempo_python = t1 - t0

    # Lista Enlazada
    lista_enlazada = ListaEnlazada()
    t0 = time.perf_counter()
    for i in range(n):
        lista_enlazada.insertar_inicio(i)
    t1 = time.perf_counter()
    tiempo_enlazada = t1 - t0

    print(f"\nInserción al inicio de {n:,} elementos:")
    print(f"  Lista de Python:  {tiempo_python:.4f} s")
    print(f"  Lista Enlazada:   {tiempo_enlazada:.4f} s")
    if tiempo_python > 0:
        print(f"  Razón:            {tiempo_python / tiempo_enlazada:.1f}× más rápida la enlazada")
    # ============================================================


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("Pruebas de ListaEnlazada")
    print("=" * 55)

 
    lista = ListaEnlazada()

    print("\n--- Insertar al inicio ---")
    lista.insertar_inicio(30)
    lista.insertar_inicio(20)
    lista.insertar_inicio(10)
    print(lista)  # esperado: cabeza → 10 → 20 → 30 → None

    print("\n--- Insertar al final ---")
    lista.insertar_final(40)
    lista.insertar_final(50)
    print(lista)  # esperado: ... → 40 → 50 → None

    print("\n--- Insertar en posición 2 ---")
    lista.insertar_en_posicion(2, 25)
    print(lista)  # esperado: 10 → 20 → 25 → 30 → 40 → 50

    print(f"\n--- Tamaño: {len(lista)} (esperado: 6) ---")

    print("\n--- Buscar ---")
    print(f"  buscar(25): {lista.buscar(25)}  (esperado: True)")
    print(f"  buscar(99): {lista.buscar(99)}  (esperado: False)")

    print("\n--- Obtener por índice ---")
    print(f"  obtener(2): {lista.obtener(2)}  (esperado: 25)")

    print("\n--- Eliminar el primero (10) ---")
    lista.eliminar(10)
    print(lista)

    print("\n--- Eliminar del medio (30) ---")
    lista.eliminar(30)
    print(lista)

    print("\n--- Eliminar el último (50) ---")
    lista.eliminar(50)
    print(lista)

    print("\n--- Eliminar valor inexistente (99) ---")
    print(f"  resultado: {lista.eliminar(99)}  (esperado: False)")
    print(lista)

    print("\n--- Invertir lista ---")
    lista.invertir()
    print(lista)  # el orden debe haberse invertido

    print("\n--- Comparación de tiempos ---")
    comparar_tiempos_insercion_inicio(n=50_000)
    