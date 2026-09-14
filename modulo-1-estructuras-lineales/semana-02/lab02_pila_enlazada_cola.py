"""
Lab 2 — Pila Enlazada, Cola y Simulador de Impresión
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Edward Hospina
Grupo: Lab B
Fecha: 14/09/2026

DECLARACIÓN DE USO DE IA:
He utilizado la herramienta de inteligencia artificial DeepSeek como apoyo
para comprender los conceptos y estructurar la lógica del laboratorio.
"""


# =============================================================================
# PARTE 1: NODO (base para la pila enlazada y la cola)
# =============================================================================

class Nodo:
    """Nodo básico con un dato y una referencia al siguiente nodo."""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # referencia al próximo nodo

"""Se le preguntó a DeepSeek con el prompt: Explícame la parte de Nodos enlazados para entender su lógica."""

# =============================================================================
# PARTE 2: PILA ENLAZADA
# =============================================================================

class PilaEnlazada:
    """
    Pila implementada con nodos enlazados.
    El tope de la pila es la cabeza de la lista de nodos.
    """

    def __init__(self):
        self._cabeza = None  # nodo del tope (None si la pila está vacía)
        self._tamanio = 0

    def push(self, dato):
        """Inserta dato en el tope. Complejidad: O(1)."""
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self._cabeza  # el nuevo apunta al antiguo tope
        self._cabeza = nuevo_nodo             # el nuevo es el tope ahora
        self._tamanio += 1

    def pop(self):
        """Elimina y retorna el dato del tope. Lanza IndexError si está vacía."""
        if self.is_empty():
            raise IndexError("No se puede hacer pop en una pila vacía")
        dato = self._cabeza.dato           # guarda el dato del tope
        self._cabeza = self._cabeza.siguiente  # avanza la cabeza al siguiente
        self._tamanio -= 1
        return dato

    def peek(self):
        """Retorna (sin eliminar) el dato del tope. Lanza IndexError si está vacía."""
        if self.is_empty():
            raise IndexError("No se puede hacer peek en una pila vacía")
        return self._cabeza.dato

    def is_empty(self):
        """Retorna True si la pila está vacía."""
        return self._cabeza is None

    def size(self):
        """Retorna el número de elementos."""
        return self._tamanio

    def __str__(self):
        """Representación: tope → ... → base"""
        if self.is_empty():
            return "Pila vacía"
        elementos = []
        actual = self._cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " → ".join(elementos)

"""Se le preguntó a DeepSeek con el prompt: Explícame la parte de Pila Enlazada."""

# =============================================================================
# PARTE 3: VERIFICADOR DE PARÉNTESIS BALANCEADOS
# =============================================================================

def parentesis_balanceados(cadena):
    """
    Retorna True si todos los pares de paréntesis, corchetes y llaves
    en `cadena` están correctamente balanceados; False en caso contrario.
    Usa la clase PilaEnlazada.
    """
    pares = {')': '(', ']': '[', '}': '{'}
    aperturas = set(pares.values())
    pila = PilaEnlazada()

    for caracter in cadena:
        if caracter in aperturas:
            # Es una apertura: la apilamos
            pila.push(caracter)
        elif caracter in pares:
            # Es un cierre: verificar que coincida con el tope
            if pila.is_empty():
                return False  # cierra sin haber abierto
            tope = pila.pop()
            if tope != pares[caracter]:
                return False  # el par no coincide

    # Al final, la pila debe estar vacía
    return pila.is_empty()

"""Se le preguntó a DeepSeek con el prompt: Explícame la Parte 
deparéntesis balanceados que aún no la entiendo bien."""

# =============================================================================
# PARTE 4: COLA (QUEUE)
# =============================================================================

class Cola:
    """
    Cola implementada con nodos enlazados.
    - enqueue agrega al final (cola)
    - dequeue saca del frente (cabeza)
    """

    def __init__(self):
        self._frente = None  # nodo del frente (primer en salir)
        self._final = None   # nodo del final (último en entrar)
        self._tamanio = 0

    def enqueue(self, dato):
        """Agrega dato al final de la cola. Complejidad: O(1)."""
        nuevo_nodo = Nodo(dato)
        if self.is_empty():
            # Si la cola está vacía, el nuevo es frente y final
            self._frente = nuevo_nodo
            self._final = nuevo_nodo
        else:
            # El actual final apunta al nuevo nodo
            self._final.siguiente = nuevo_nodo
            # El nuevo nodo es el nuevo final
            self._final = nuevo_nodo
        self._tamanio += 1

    def dequeue(self):
        """Elimina y retorna el dato del frente. Lanza IndexError si está vacía."""
        if self.is_empty():
            raise IndexError("No se puede hacer dequeue en una cola vacía")
        dato = self._frente.dato             # guarda el dato del frente
        self._frente = self._frente.siguiente  # avanza el frente
        self._tamanio -= 1
        # Si la cola quedó vacía, el final también debe ser None
        if self._frente is None:
            self._final = None
        return dato

    def front(self):
        """Retorna (sin eliminar) el dato del frente. Lanza IndexError si está vacía."""
        if self.is_empty():
            raise IndexError("No se puede hacer front en una cola vacía")
        return self._frente.dato

    def is_empty(self):
        return self._frente is None

    def size(self):
        return self._tamanio

    def __str__(self):
        """Representación: frente → ... → final"""
        if self.is_empty():
            return "Cola vacía"
        elementos = []
        actual = self._frente
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " → ".join(elementos)

"""Se le preguntó a DeepSeek con el prompt: Explícame la sección Cola."""

# =============================================================================
# PARTE 5: SIMULADOR DE COLA DE IMPRESIÓN (mini-proyecto)
# =============================================================================

class TrabajoImpresion:
    """Representa un trabajo en la cola de impresión."""

    def __init__(self, nombre, paginas):
        self.nombre = nombre
        self.paginas = paginas

    def __str__(self):
        return f"'{self.nombre}' ({self.paginas} pág.)"


def simulador_impresion(trabajos):
    """
    Simula una cola de impresión. Recibe una lista de tuplas (nombre, páginas).
    Imprime en orden de llegada (FIFO) el nombre de cada trabajo y cuántas páginas tiene.
    Al final muestra el total de páginas impresas.
    """
    cola = Cola()

    # 1. Encolar todos los trabajos
    print("Encolando trabajos...")
    for nombre, paginas in trabajos:
        trabajo = TrabajoImpresion(nombre, paginas)
        cola.enqueue(trabajo)
        print(f"   + {trabajo}")

    print(f"\nTotal en cola: {cola.size()} trabajos\n")

    # 2. Procesar la cola (FIFO)
    print("Procesando cola de impresión...")
    total_paginas = 0
    numero = 1
    while not cola.is_empty():
        trabajo = cola.dequeue()
        total_paginas += trabajo.paginas
        print(f"   {numero}. Imprimiendo {trabajo}")
        numero += 1

    # 3. Mostrar total
    print(f"\nTotal de páginas impresas: {total_paginas}")


# =============================================================================
# PARTE 6: EVALUACIÓN DE NOTACIÓN POSTFIJA (Tarea autónoma)
# =============================================================================

def evaluar_postfija(expresion):
    """
    Evalúa una expresión en notación postfija (RPN) usando PilaEnlazada.

    Ejemplo: "3 4 + 5 *" → 35
    Algoritmo:
      - Si el token es un número → push
      - Si es un operador → pop dos veces (b, a) y aplicar a OP b
    """
    pila = PilaEnlazada()
    operadores = {'+', '-', '*', '/'}

    for token in expresion.split():
        if token in operadores:
            if pila.size() < 2:
                raise ValueError(f"Expresión postfija inválida: {expresion}")
            b = pila.pop()
            a = pila.pop()
            if token == '+':
                resultado = a + b
            elif token == '-':
                resultado = a - b
            elif token == '*':
                resultado = a * b
            elif token == '/':
                resultado = a / b
            pila.push(resultado)
        else:
            pila.push(float(token))

    if pila.size() != 1:
        raise ValueError(f"Expresión postfija inválida: {expresion}")
    return pila.pop()


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("PARTE 2: Pila Enlazada")
    print("=" * 55)

    # Caso 1: Pila vacía
    pila = PilaEnlazada()
    print(f"Pila vacía? {pila.is_empty()}")   # True
    print(f"Tamaño: {pila.size()}")           # 0

    # Caso 2: Push
    pila.push(1)
    pila.push(2)
    pila.push(3)
    print(f"Después de push 1,2,3 → {pila}")  # 3 → 2 → 1
    print(f"Tamaño: {pila.size()}")           # 3

    # Caso 3: Peek
    print(f"Tope (peek): {pila.peek()}")      # 3
    print(f"Tamaño tras peek: {pila.size()}") # 3

    # Caso 4: Pop
    print(f"Pop: {pila.pop()}")               # 3
    print(f"Pila ahora: {pila}")              # 2 → 1
    print(f"Tamaño tras pop: {pila.size()}")  # 2

    # Caso 5: Pop en pila vacía
    pila_vacia = PilaEnlazada()
    try:
        pila_vacia.pop()
        print("ERROR: no se lanzó IndexError")
    except IndexError as e:
        print(f"IndexError capturado: {e}")

    print("\n" + "=" * 55)
    print("PARTE 3: Verificador de Paréntesis Balanceados")
    print("=" * 55)
    casos = [
        ("({[]})", True),
        ("([)]", False),
        ("{[", False),
        ("", True),
        ("3 + (4 * [2])", True),
        ("(()", False),
        (")(", False),
    ]
    for cadena, esperado in casos:
        resultado = parentesis_balanceados(cadena)
        estado = "OK" if resultado == esperado else "ERROR"
        print(f"  [{estado}] '{cadena}' → {resultado} (esperado: {esperado})")

    print("\n" + "=" * 55)
    print("PARTE 4: Cola")
    print("=" * 55)

    # Caso 1: Cola vacía
    cola = Cola()
    print(f"Cola vacía? {cola.is_empty()}")   # True

    # Caso 2: Enqueue
    cola.enqueue("A")
    cola.enqueue("B")
    cola.enqueue("C")
    print(f"Después de enqueue A,B,C → {cola}")  # A → B → C
    print(f"Tamaño: {cola.size()}")              # 3

    # Caso 3: Front (sin eliminar)
    print(f"Frente (front): {cola.front()}")     # A
    print(f"Tamaño tras front: {cola.size()}")   # 3

    # Caso 4: Dequeue (FIFO)
    print(f"Dequeue: {cola.dequeue()}")          # A
    print(f"Cola ahora: {cola}")                 # B → C
    print(f"Dequeue: {cola.dequeue()}")          # B
    print(f"Cola ahora: {cola}")                 # C

    # Caso 5: Dequeue en cola vacía
    cola_vacia = Cola()
    try:
        cola_vacia.dequeue()
        print("ERROR: no se lanzó IndexError")
    except IndexError as e:
        print(f"IndexError capturado: {e}")

    print("\n" + "=" * 55)
    print("PARTE 5: Simulador de Impresión")
    print("=" * 55)
    trabajos = [("Tesis cap1", 12), ("Factura", 1), ("Informe anual", 8), ("CV", 2)]
    simulador_impresion(trabajos)

    print("\n" + "=" * 55)
    print("PARTE 6: Evaluación Postfija (tarea autónoma)")
    print("=" * 55)
    expresiones = [
        ("3 4 +", 7.0),
        ("3 4 + 5 *", 35.0),
        ("5 1 2 + 4 * + 3 -", 14.0),
        ("10 2 /", 5.0),
    ]
    for expr, esperado in expresiones:
        resultado = evaluar_postfija(expr)
        estado = "OK" if resultado == esperado else "ERROR"
        print(f"  [{estado}] '{expr}' → {resultado} (esperado: {esperado})")