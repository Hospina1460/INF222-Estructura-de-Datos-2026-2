"""
Lab 1 — Implementación de la clase Pila (Stack)
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Edward Hospina
Grupo: 
Fecha: 04/09/2026

DECLARACIÓN DE USO DE IA:
He utilizado la herramienta de inteligencia artificial DeepSeek (específicamente, su modelo de chat) 
como apoyo para comprender los conceptos y estructurar la lógica de la implementación de la clase Pila.
"""


class Pila:
    """
    Implementación de una pila (stack) usando una lista de Python como
    contenedor interno. Principio LIFO: el último elemento insertado es
    el primero en salir.
    """

    def __init__(self):
        """Inicializa una pila vacía."""
        self._datos = []  # el tope de la pila está en el índice -1

    def push(self, dato):
        """
        Agrega `dato` al tope de la pila.
        Complejidad: O(1) amortizado.
        """
        self._datos.append(dato)

    def pop(self):
        """
        Elimina y retorna el elemento del tope de la pila.
        Lanza IndexError si la pila está vacía.
        Complejidad: O(1) amortizado.
        """
        if self.is_empty():
            raise IndexError("No se puede hacer pop en una pila vacía")
        return self._datos.pop()

    def peek(self):
        """
        Retorna (sin eliminar) el elemento del tope de la pila.
        Lanza IndexError si la pila está vacía.
        Complejidad: O(1).
        """
        if self.is_empty():
            raise IndexError("No se puede hacer peek en una pila vacía")
        return self._datos[-1]

    def is_empty(self):
        """
        Retorna True si la pila no contiene elementos, False en caso contrario.
        Complejidad: O(1).
        """
        return len(self._datos) == 0

    def size(self):
        """
        Retorna el número de elementos en la pila.
        Complejidad: O(1).
        """
        return len(self._datos)

    def __str__(self):
        """
        Retorna una representación legible de la pila.
        Formato sugerido: Pila (tope -> base): [3, 2, 1]
        Complejidad: O(n).
        """
        elementos = [str(item) for item in reversed(self._datos)]
        return f"Pila (tope -> base): [{', '.join(elementos)}]"


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("Pruebas de la clase Pila")
    print("=" * 50)

    # Caso 1: Pila vacía
    print("\n--- Caso 1: Pila vacía ---")
    pila1 = Pila()
    print(f"¿Está vacía? {pila1.is_empty()}")  # Debe ser True
    print(f"Tamaño: {pila1.size()}")  # Debe ser 0
    print(f"Representación: {pila1}")

    # Caso 2: push de 3 elementos
    print("\n--- Caso 2: Push de 3 elementos ---")
    pila2 = Pila()
    pila2.push(10)
    pila2.push(20)
    pila2.push(30)
    print(f"Después de push(10), push(20), push(30): {pila2}")
    print(f"Tamaño: {pila2.size()}")  # Debe ser 3
    print(f"¿Está vacía? {pila2.is_empty()}")  # Debe ser False

    # Caso 3: peek sin modificar la pila
    print("\n--- Caso 3: Peek sin modificar ---")
    pila3 = Pila()
    pila3.push(100)
    pila3.push(200)
    pila3.push(300)
    print(f"Pila antes de peek: {pila3}")
    tope = pila3.peek()
    print(f"Tope retornado por peek: {tope}")  # Debe ser 300
    print(f"Pila después de peek (sin cambios): {pila3}")
    print(f"Tamaño después de peek: {pila3.size()}")  # Sigue siendo 3

    # Caso 4: pop retorna el tope
    print("\n--- Caso 4: Pop retorna el tope ---")
    pila4 = Pila()
    pila4.push(1)
    pila4.push(2)
    pila4.push(3)
    print(f"Pila antes de pop: {pila4}")
    elemento = pila4.pop()
    print(f"Elemento retornado por pop: {elemento}")  # Debe ser 3
    print(f"Pila después de pop: {pila4}")
    print(f"Tamaño después de pop: {pila4.size()}")  # Debe ser 2

    # Caso 5: pop en pila vacía lanza IndexError
    print("\n--- Caso 5: Pop en pila vacía ---")
    pila5 = Pila()
    try:
        pila5.pop()
        print("ERROR: No se lanzó la excepción esperada")
    except IndexError as e:
        print(f"Excepción capturada correctamente: {e}")
        print("La excepción IndexError se lanzó como se esperaba")

    # Caso 6: Prueba adicional - múltiples pops
    print("\n--- Caso 6: Múltiples pops ---")
    pila6 = Pila()
    for i in range(1, 6):  # Agregar 1, 2, 3, 4, 5
        pila6.push(i)
    print(f"Pila inicial: {pila6}")
    
    # Hacer pop de todos los elementos
    while not pila6.is_empty():
        elemento = pila6.pop()
        print(f"Pop: {elemento}, Pila queda: {pila6}")
    
    print(f"Pila final vacía: {pila6.is_empty()}")

    # Caso 7: Prueba con diferentes tipos de datos
    print("\n--- Caso 7: Diferentes tipos de datos ---")
    pila7 = Pila()
    pila7.push("Hola")
    pila7.push(3.1416)
    pila7.push(True)
    pila7.push(None)
    print(f"Pila con diferentes tipos: {pila7}")
    print(f"Tope: {pila7.peek()}")  # Debe ser None
    print(f"Tamaño: {pila7.size()}")  # Debe ser 4

    # Caso 8: Verificar que el orden LIFO se mantiene
    print("\n--- Caso 8: Verificar orden LIFO ---")
    pila8 = Pila()
    datos = ["primero", "segundo", "tercero", "cuarto"]
    for dato in datos:
        pila8.push(dato)
    
    print(f"Orden de inserción: {datos}")
    print(f"Pila: {pila8}")
    
    # Los elementos deben salir en orden inverso
    print("Orden de salida (LIFO):")
    while not pila8.is_empty():
        print(f"  {pila8.pop()}")