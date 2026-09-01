# TP Listas de una dimensión

# Ejercicio 1: Suma de Elementos
lista = input("Ingrese una lista de números: ").split()

numeros = []

for elemento in lista:
    numero = int(elemento)
    numeros.append(numero)

suma = sum(numeros)

print(f"Suma de todos los elementos de la lista: {suma}")

# Ejercicio 2: Encontrar el Mayor y el Menor
lista = input("Ingrese una lista de números: ").split()

numeros = []

for elemento in lista:
    numero = int(elemento)
    numeros.append(numero)

mayor = max(numeros)
menor = min(numeros)

print(f"Número mayor de la lista: {mayor}")
print(f"Número menor de la lista: {menor}")

# Ejercicio 3: Invertir una Lista
lista = input("Ingrese una lista: ").split()

lista.reverse()

print(f"Lista invertida: {lista}")

# Ejercicio 4: Contar Elementos Pares e Impares
pares = [x for x in numeros if x % 2 == 0]
impares = [x for x in numeros if x % 2 != 0]

print(f"Cantidad de números pares: {len(pares)}")
print(f"Cantidad de números impares: {len(impares)}")

# Ejercicio 5: Multiplicar Elementos por un Valor
lista = input("Ingrese una lista de números: ").split()

multiplicador = int(input("Ingrese un número: "))

numeros = []

for elemento in lista:
    numero = int(elemento)
    numeros.append(numero)

resultado = [x * multiplicador for x in numeros]

print(f"Lista multiplicada por {multiplicador}: {resultado}")

# Ejercicio 6: Eliminar Duplicados
lista = (input("Ingrese una lista de números: ")).split()

numeros = []

for elemento in lista:
    numero = int(elemento)
    numeros.append(numero)

lista_sin_repetidos = list(set(numeros))

print(f"Lista sin repeticiones: {lista_sin_repetidos} ")

# Ejercicio 7: Promedio de una Lista
lista = input("Ingrese una lista de números: ").split()

numeros = []

for elemento in lista:
    numero = int(elemento)
    numeros.append(numero)

suma = sum(numeros)
elementos = len(numeros)

promedio = suma / elementos

print(f"Promedio de la lista: {promedio}")

# Ejercicio 8: Encontrar Elementos Repetidos
lista = [1, 2, 3, 2, 4, 1, 5]

vistos = set()
repetidos = set()

for elemento in lista:
    if elemento in vistos:
        repetidos.add(elemento)
    else:
        vistos.add(elemento)

print(f"Lista original: {lista}")
print(f"Elementos repetidos: {repetidos}")

# Ejercicio 9: Lista de Números Primos
def es_primo(numero):
    if numero < 2:
        return False

    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False

    return True

lista = input("Ingrese una lista de números: ").split()

numeros_primos = []

for numero in lista:
    numero = int(numero)

    if es_primo(numero):
        numeros_primos.append(numero)

print(f"Números primos de la lista: {numeros_primos}")

# Ejercicio 10: Eliminar un Elemento por su Índice
lista = input("Ingrese una lista de números: ").split()

numeros = []

for elemento in lista:
    numero = int(elemento)
    numeros.append(numero)

print(numeros)

indice = int(input("Ingrese el índice que desea eliminar: "))

del numeros[indice]

print(numeros)

# Ejercicio 11: Contar Ocurrencias de un Elemento
lista = input("Ingrese una lista de números: ").split()
num = int(input("Ahora, introduzca un número: "))

numeros = []
contador = 0

for elemento in lista:
    numero = int(elemento)
    numeros.append(numero)

    if numero == num:
        contador += 1

print(f"El número {num} aparece {contador} veces en la lista.")

# Ejercicio 12: Sumar Listas Elemento por Elemento
lista1 = input("Ingrese una lista de números: ").split()
lista2 = input("Ingrese otra lista de números con la misma longitud: ").split()

numeros1 = []
numeros2 = []

for elemento in lista1:
    numero1 = int(elemento)
    numeros1.append(numero1)

for elemento in lista2:
    numero2 = int(elemento)
    numeros2.append(numero2)

sumas = []

for i in range(len(numeros1)):
    suma = numeros1[i] + numeros2[i]
    sumas.append(suma)

print(f"Suma de las listas: {sumas}")

# Ejercicio 13: Explique y ejemplifique la librería NumPy para trabajar con matrices y arrays

# NumPy es una librería de Python utilizada principalmente para trabajar con datos numéricos, arrays y matrices. 
# Permite realizar operaciones matemáticas de forma sencilla y eficiente.

# Para utilizarla se importa mediante import numpy as np.

# Un array es una estructura similar a una lista, pero está especialmente diseñada para trabajar con datos numéricos. Por ejemplo:

# import numpy as np

# numeros = np.array([1, 2, 3, 4])
# print(numeros * 2)

# El resultado sería: [2 4 6 8]

# También permite trabajar con matrices, que son arrays de dos dimensiones. Por ejemplo:

# matriz = np.array([
#    [1, 2, 3],
#    [4, 5, 6]
# ])

# Esta matriz tiene 2 filas y 3 columnas. NumPy permite realizar operaciones y acceder a sus elementos mediante índices.

# TP Listas Bidimensionales

# Ejercicio 1: Crear una Matriz de Números
def crear_matriz(filas, columnas):
    matriz = []
    contador = 1

    for i in range(filas):
        fila_actual = []

        for j in range(columnas):
            fila_actual.append(contador)
            contador += 1

        matriz.append(fila_actual)

    return matriz

filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

matriz = crear_matriz(filas, columnas)

print(matriz)

# Ejercicio 2: Suma de Todos los Elementos
suma_total = sum(sum(fila) for fila in matriz)

print(f"Suma total: {suma_total}")

# Ejercicio 3: Suma de Cada Fila
suma_fila = [sum(fila) for fila in matriz]

print(f"Suma fila: {suma_fila})")

# Ejercicio 4: Matriz Transpuesta
transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

print(transpuesta)

# Ejercicio 5: Encontrar el Elemento Mayor
numeros = []

for fila in matriz:
    for elemento in fila:
        numeros.append(elemento)

mayor = max(numeros)
print(f"Número Mayor: {mayor}")

# Ejercicio 6: Multiplicar una Matriz por un Escalar
escalar = int(input("Ingrese un valor escalar: "))

resultado = []

for fila in matriz:
    nueva_fila = []
    for elemento in fila:
        nueva_fila.append(elemento * escalar)
    resultado.append(nueva_fila)

print(resultado)

# Ejercicio 7: Diagonal de una Matriz Cuadrada
matriz_cuadrada = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

for contador in range(len(matriz_cuadrada)):
    elemento = matriz_cuadrada[contador][contador]
    print(elemento)

# Ejercicio 8: Matriz Identidad
n = int(input("Ingrese el tamaño de la matriz: "))

identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

print("Matriz identidad:")

for fila in identidad:
    print(fila)

# Ejercicio 9: Matriz Identidad Inversa
n = int(input("Ingrese el tamaño de la matriz: "))

identidad_inversa = [[1 if j == n - 1 - i else 0 for j in range(n)] for i in range(n)]

print("Matriz identidad inversa:")

for fila in identidad_inversa:
    print(fila)

# Ejercicio 10: Verificar Matriz Simétrica
print(f"Matriz: {matriz}")
print(f"Transpuesta: {transpuesta}")

if matriz == transpuesta:
    print("Matriz simétrica.")
else:
    print("Matriz no simétrica.")

# Ejercicio 11: Rotar una Matriz 90 Grados
nueva_matriz = []

for columna in range(len(matriz[0])):
    nueva_fila = []

    for fila in range(len(matriz) - 1, -1, -1):
        nueva_fila.append(matriz[fila][columna])

    nueva_matriz.append(nueva_fila)

print(nueva_matriz)

# Ejercicio 12: Analizador y Filtrado de Calificaciones
lista = "45, 88, -5, 92, 30, 110, 75, 60, 15".split(",")

notas = []
aprobados = []
reprobados = []
suma = 0
cantidad = 0

for nota in lista:
    numero = int(nota)
    notas.append(numero)

    if numero < 0 or numero > 100:
        continue

    elif numero >= 60:
        aprobados.append(numero)
        suma += numero
        cantidad += 1

    else:
        reprobados.append(numero)
        suma += numero
        cantidad += 1

promedio = suma / cantidad
ultimos_aprobados = aprobados[-2:]

print(f"Lista de aprobados: {aprobados}")
print(f"Lista de reprobados: {reprobados}")
print(f"Promedio total: {promedio:.2f}")
print(f"Últimos 2 aprobados: {ultimos_aprobados}")

# Ejercicio 13: Gestor Interactivo de Proyectos con while y Operador in
tareas = []

while True:

    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Ver resumen")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        nombre_tarea = input("Ingrese el nombre de la tarea que desea agregar: ")

        if nombre_tarea in tareas:
            print("Ya está registrada.")
        else:
            tareas.append(nombre_tarea)

    elif opcion == "2":
        nombre_tarea = input("Ingrese el nombre de la tarea que desea eliminar: ")

        if nombre_tarea in tareas:
            tareas.remove(nombre_tarea)
        else:
            print("No se encontró una tarea con ese nombre.")

    elif opcion == "3":
        print(f"Total de tareas registradas: {len(tareas)}")
        primeras_tres = tareas[:3]
        print(f"Primeras 3 tareas de la lista: {primeras_tres}")

    elif opcion == "4":
        break
    

