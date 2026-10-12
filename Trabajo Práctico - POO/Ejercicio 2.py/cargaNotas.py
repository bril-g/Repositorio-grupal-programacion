from nota import Nota
from alumno import Alumno

class CargaNotas:
    def __init__(self):
        self.alumnos = []

    def main(self):
        salirAlumno = False

        while not salirAlumno:
            print("--- Ingrese datos del alumno ---")
            nombreCompleto = input("Nombre completo: ")
            legajo = int(input("Legajo: "))

            notas = []
            salirNotas = False

            while not salirNotas:
                catedra = input("Catedra: ")
                notaExamen = float(input("Nota examen: "))
                notas.append(Nota(catedra, notaExamen))
                salir = input("¿Desea salir de la carga de notas (s/n)? ")
                if salir == "s":
                    salirNotas = True

            self.alumnos.append(Alumno(nombreCompleto, legajo, notas))

            salir = input("¿Desea salir de la carga de alumnos (s/n)? ")
            if salir == "s":
                salirAlumno = True

        for alumno in self.alumnos:
            print(f"Datos alumno: {alumno}")
            for nota in alumno.notas:
                print(f"Nota: {nota}")
            promedio = alumno.promedio()   
            print(f"El promedio del alumno es: {promedio}")   


c = CargaNotas()
c.main()   
        


