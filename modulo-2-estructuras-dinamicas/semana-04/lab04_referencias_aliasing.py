"""
Lab 4 — Referencias y Aliasing en Python
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Edward Hospina
Grupo: Lab B
Fecha: 30/09/2026

DECLARACIÓN DE USO DE IA:
He utilizado la herramienta de inteligencia artificial DeepSeek como apoyo
para comprender los conceptos de referencias, aliasing y copias en Python.

Instrucciones:
    Para cada fragmento de código, PRIMERO escribe tu predicción en el comentario
    "PREDICCIÓN:", LUEGO ejecuta y registra el resultado real en "RESULTADO:".
    Usa Python Tutor para visualizar el estado de la memoria.
"""

import copy

print("=" * 55)
print("PARTE 1 — id() y referencias básicas")
print("=" * 55)

# Experimento 1.1: referencias a enteros
a = 42
b = a
# PREDICCIÓN: ¿son a y b el mismo objeto? (id(a) == id(b) → True/False)
# Tu predicción: True
print(f"1.1 id(a) == id(b): {id(a) == id(b)}")
# RESULTADO: True
# EXPLICACIÓN: Al hacer b = a, b no crea un nuevo objeto, simplemente
#              copia la referencia. Python reutiliza el mismo objeto 42.

# Experimento 1.2: reasignación no afecta al original
a = 42
b = a
b = 99
# PREDICCIÓN: ¿qué valor tiene a después de b = 99?
# Tu predicción: a = 42
print(f"1.2 a = {a}  (b fue reasignado a 99)")
# RESULTADO: 42
# EXPLICACIÓN: b = 99 no modifica el objeto 42. Lo que hace
#              es que b ahora apunte a un objeto diferente, el 99. a sigue
#              apuntando al 42 original.

print("\n" + "=" * 55)
print("PARTE 2 — Aliasing con listas")
print("=" * 55)

# Experimento 2.1: aliasing
lista_a = [1, 2, 3]
lista_b = lista_a          # ← esto NO copia la lista
lista_b.append(99)
# PREDICCIÓN: ¿qué contiene lista_a?
# Tu predicción: lista_a = [1, 2, 3, 99]
print(f"2.1 lista_a = {lista_a}  (lista_b.append(99))")
# RESULTADO: [1, 2, 3, 99]
# EXPLICACIÓN: lista_b = lista_a              
#              Ambas variables apuntan al MISMO objeto lista. Al hacer
#              lista_b.append(99), se muta el objeto compartido, así que
#              lista_a también ve el cambio.

# Experimento 2.2: copia superficial (shallow copy)
lista_a = [1, 2, 3]
lista_c = lista_a.copy()   # ← esto SÍ crea una copia nueva
lista_c.append(99)
# PREDICCIÓN: ¿qué contiene lista_a ahora?
# Tu predicción: lista_a = [1, 2, 3]
print(f"2.2 lista_a = {lista_a}  (lista_c.copy() y lista_c.append(99))")
# RESULTADO: [1, 2, 3]
# EXPLICACIÓN: .copy() crea una nueva lista con los mismos elementos.
#              lista_c es un objeto independiente. Al hacer append en
#              lista_c, solo se modifica esa copia, no la original.

# Experimento 2.3: copia superficial con listas anidadas
original = [[1, 2], [3, 4]]
copia_superficial = original.copy()
copia_superficial[0].append(99)   # modifica la sublista
# PREDICCIÓN: ¿qué contiene original[0]?
# Tu predicción: original[0] = [1, 2, 99]
print(f"2.3 original[0] = {original[0]}  (shallow copy + append interno)")
# RESULTADO: [1, 2, 99]
# EXPLICACIÓN: Cuando hago copia_superficial[0].append(99),
#              estoy modificando la sublista [1, 2] que es compartida, así
#              que original[0] también refleja el cambio: pasa de [1, 2]
#              a [1, 2, 99].

# Experimento 2.4: copia profunda (deep copy)
original = [[1, 2], [3, 4]]
copia_profunda = copy.deepcopy(original)
copia_profunda[0].append(99)
# PREDICCIÓN: ¿qué contiene original[0] ahora?
# Tu predicción: original[0] = [1, 2]
print(f"2.4 original[0] = {original[0]}  (deep copy + append interno)")
# RESULTADO: [1, 2]
# EXPLICACIÓN: deepcopy() copia todo, incluidas las
#              sublistas. copia_profunda[0] es una lista nueva e
#              independiente. No afecta a original[0].

print("\n" + "=" * 55)
print("PARTE 3 — Funciones: mutar vs. retornar copia")
print("=" * 55)


def agregar_elemento_in_situ(lista, elemento):
    """Modifica la lista original (mutación in situ)."""
    lista.append(elemento)
    # No retorna nada (retorna None implícitamente)


def agregar_elemento_copia(lista, elemento):
    """
    Retorna una nueva lista con el elemento agregado.
    La lista original NO se modifica.
    """
    nueva_lista = lista.copy()   
    nueva_lista.append(elemento) 
    return nueva_lista           


# Prueba de mutar in situ
mi_lista = [1, 2, 3]
agregar_elemento_in_situ(mi_lista, 4)
print(f"3.1 in_situ:  mi_lista = {mi_lista}  (esperado: [1, 2, 3, 4])")

# Prueba de retornar copia
mi_lista = [1, 2, 3]
nueva_lista = agregar_elemento_copia(mi_lista, 4)
print(f"3.2 copia:    mi_lista  = {mi_lista}   (esperado: [1, 2, 3] — sin cambios)")
print(f"              nueva_lista = {nueva_lista}  (esperado: [1, 2, 3, 4])")

print("\n" + "=" * 55)
print("PARTE 4 — Predicciones adicionales (escribe ANTES de ejecutar)")
print("=" * 55)

# Fragmento 4.1
x = [10, 20, 30]
y = x
x = [40, 50]  # reasignación (no mutación)
# PREDICCIÓN: ¿qué contiene y?
# Tu predicción: y = [10, 20, 30]
print(f"4.1 y = {y}")
# RESULTADO: [10, 20, 30]
# EXPLICACIÓN: x = [40, 50] no muta la lista original, solo reasigna x
#              para que apunte a una lista nueva. y sigue apuntando a
#              la lista original [10, 20, 30].

# Fragmento 4.2
def modificar(lst):
    lst += [99]   # ¿es esto lo mismo que lst.append(99)?

nums = [1, 2, 3]
modificar(nums)1
# PREDICCIÓN: ¿qué contiene nums?
# Tu predicción: nums = [1, 2, 3, 99]
print(f"4.2 nums = {nums}")
# RESULTADO: [1, 2, 3, 99]
# EXPLICACIÓN: lst += [99] no es lo mismo que lst.append(99).
#              En este ejemplo da el mismo resultado pero no 
#              en todos los casos da el mismo resultado.                 
#              



# NOTA: += en listas llama a __iadd__ que modifica in situ,
#       mientras que + crea una lista nueva.

print("\n" + "=" * 55)
print("PARTE 5 — Verificación adicional con id()")
print("=" * 55)

# Verificamos el caso 1.1 con más detalle
a = 42
b = a
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print(f"¿Mismo objeto? {a is b}")

# Verificamos el caso 2.1 con más detalle
lista_a = [1, 2, 3]
lista_b = lista_a
print(f"\nid(lista_a) = {id(lista_a)}")
print(f"id(lista_b) = {id(lista_b)}")
print(f"¿Mismo objeto? {lista_a is lista_b}")

# Después de copiar
lista_c = lista_a.copy()
print(f"\nid(lista_c) = {id(lista_c)}")
print(f"¿Mismo objeto que lista_a? {lista_a is lista_c}")