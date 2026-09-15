from funciones import *

lista_alumnos, dicc_alumnos = leer_alumnos()

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Ver alumnos")
    print("2. Agregar alumno")
    print("3. Generar y mostrar archivo de aprobados")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":

        if len(lista_alumnos) == 0:
            print("\nNo hay alumnos en el archivo.")

        else:
            print("\n--- LISTA DE ALUMNOS ---")

            for alumno in lista_alumnos:
                print(f"Alumno: {alumno[0]} {alumno[1]} | Nota Promedio: {alumno[3]}")

    elif opcion == "2":
        agregar_alumno(lista_alumnos, dicc_alumnos)

    elif opcion == "3":
        guardar_aprobados(lista_alumnos)

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intente nuevamente.")