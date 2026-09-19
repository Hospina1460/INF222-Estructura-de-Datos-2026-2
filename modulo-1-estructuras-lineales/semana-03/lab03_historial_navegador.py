"""
Lab 3 — Simulador de Historial de Navegador (Taller Integrador)
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Edward Hospina
Grupo: Lab B
Fecha: 19/09/2026

Descripción:
    Simula el comportamiento del historial de un navegador web usando DOS pilas:
    - pila_atras:    páginas a las que se puede volver
    - pila_adelante: páginas a las que se puede avanzar
    Usa la clase Pila de lab01 o PilaEnlazada de lab02 (elige una y cópiala aquí o impórtala).
"""


class Pila:
    """Copia de la clase Pila implementada en lab01 (completa tu implementación aquí)."""

    def __init__(self):
        self._datos = []

    def push(self, dato):
        self._datos.append(dato)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop en pila vacía")
        return self._datos.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek en pila vacía")
        return self._datos[-1]

    def is_empty(self):
        return len(self._datos) == 0

    def size(self):
        return len(self._datos)

    def __str__(self):
        return f"Pila (tope→base): {list(reversed(self._datos))}"


class HistorialNavegador:
    """
    Simula el historial de un navegador web con botones Atrás y Adelante.
    """

    def __init__(self, pagina_inicial="about:blank"):
        self._actual = pagina_inicial
        self._pila_atras = Pila()
        self._pila_adelante = Pila()
 
    def visitar(self, url):
        self._pila_atras.push(self._actual)
        self._actual = url
        while not self._pila_adelante.is_empty():
            self._pila_adelante.pop()

    def atras(self):
        if self._pila_atras.is_empty():
            return None
        self._pila_adelante.push(self._actual)
        self._actual = self._pila_atras.pop()
        return self._actual

    def adelante(self):
        if self._pila_adelante.is_empty():
            return None
        self._pila_atras.push(self._actual)
        self._actual = self._pila_adelante.pop()
        return self._actual

    def pagina_actual(self):
        return self._actual

    def estado(self):
        print(f"  Actual:   {self._actual}")
        print(f"  Atrás:    {self._pila_atras}")
        print(f"  Adelante: {self._pila_adelante}")


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("Simulador de Historial de Navegador")
    print("=" * 55)

    nav = HistorialNavegador()

    print("\n--- Visitando páginas ---")
    nav.visitar("google.com")
    nav.visitar("wikipedia.org")
    nav.visitar("github.com")
    nav.visitar("up.ac.pa")
    print(f"Página actual: {nav.pagina_actual()}")
    nav.estado()

    print("\n--- Navegando Atrás x2 ---")
    print(f"  → {nav.atras()}")
    print(f"  → {nav.atras()}")
    print(f"Página actual: {nav.pagina_actual()}")
    nav.estado()

    print("\n--- Navegando Adelante x1 ---")
    print(f"  → {nav.adelante()}")
    print(f"Página actual: {nav.pagina_actual()}")
    nav.estado()

    print("\n--- Visitar nueva página (borra el adelante) ---")
    nav.visitar("classroom.github.com")
    print(f"Página actual: {nav.pagina_actual()}")
    nav.estado()

    print("\n--- Intentar adelante cuando no hay ---")
    resultado = nav.adelante()
    print(f"  → {resultado}  (esperado: None)")

    print("\n--- Intentar atrás hasta el inicio ---")
    while nav.atras() is not None:
        pass
    print(f"Página actual: {nav.pagina_actual()}  (esperado: about:blank)")
    resultado_extra = nav.atras()
    print(f"Otro atrás → {resultado_extra}  (esperado: None)")