def cargarNotas(materias):

    for materia in materias:

        print(f"\nIngrese las notas para la materia {materia[0]}")

        nota1 = float(input("Nota 1: "))

        while nota1 < 0 or nota1 > 10:
            print("La nota debe estar entre 0 y 10.")
            nota1 = float(input("Nota 1: "))

        materia[1] = nota1

        nota2 = float(input("Nota 2: "))

        while nota2 < 0 or nota2 > 10:
            print("La nota debe estar entre 0 y 10.")
            nota2 = float(input("Nota 2: "))

        materia[2] = nota2

        notaFinal = (nota1 + nota2) / 2
        materia[3] = notaFinal

        print(f"Nota Final: {notaFinal}")


def mostrarMaterias(materias):

    print("\nLista de materias:")
    print(materias)


def buscarMayorNota(materias):

    mayorNota = 0
    materiaMayor = ""

    for fila in materias:

        if fila[1] > mayorNota:
            mayorNota = fila[1]
            materiaMayor = fila[0]

        if fila[2] > mayorNota:
            mayorNota = fila[2]
            materiaMayor = fila[0]

    print(f"La nota más alta es {mayorNota} y corresponde a {materiaMayor}")


def calcularPromedio(materias):

    sumaNotasFinales = 0

    for fila in materias:
        sumaNotasFinales += fila[3]

    promedioGeneral = sumaNotasFinales / len(materias)

    print(f"Promedio general: {promedioGeneral}")

    return promedioGeneral


def buscarMejorAlumno(notasFinales):

    mayorPromedio = 0
    mejorAlumno = ""

    for promedio in notasFinales:

        if promedio[1] > mayorPromedio:
            mayorPromedio = promedio[1]
            mejorAlumno = promedio[0]

    print("\nNotas finales:")
    print(notasFinales)

    print(f"\nEl promedio más alto es {mayorPromedio} y corresponde a {mejorAlumno}")