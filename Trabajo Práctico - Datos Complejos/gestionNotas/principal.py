from datos import *
from funciones import *


for legajo, nombre in alumnos.items():

    print(f"\nAlumno: {nombre}")

    cargarNotas(materias)

    mostrarMaterias(materias)

    buscarMayorNota(materias)

    promedioGeneral = calcularPromedio(materias)

    print(f"Promedio general: {promedioGeneral}")

    notasFinales.append([nombre, promedioGeneral])


buscarMejorAlumno(notasFinales)