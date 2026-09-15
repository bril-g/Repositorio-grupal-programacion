def validar_existe_alumno(legajo, diccionario):
    return legajo in diccionario


def leer_alumnos():
    alumnos_lista = []
    alumnos_dicc = {}

    archivo_crear = open("alumnos.txt", "a")
    archivo_crear.close()

    with open("alumnos.txt", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            
            if linea:
                partes = linea.split(";")
                
                nombre = partes[0]
                apellido = partes[1]
                legajo = partes[2]
                promedio = partes[3]

                alumnos_lista.append(partes)

                alumnos_dicc[legajo] = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "promedio": promedio
                }

    return alumnos_lista, alumnos_dicc


def agregar_alumno(alumnos_lista, alumnos_dicc):
    print("--- INGRESO DE NUEVO ALUMNO ---")

    nombre = input("Nombre: ").title()

    while not nombre.isalpha():
        print("Error: El nombre solo debe contener letras.")
        nombre = input("Nombre: ").title()

    apellido = input("Apellido: ").title()

    while not apellido.isalpha():
        print("Error: El apellido solo debe contener letras.")
        apellido = input("Apellido: ").title()

    legajo = input("Legajo (5 dígitos): ")

    while len(legajo) != 5 or not legajo.isdigit():
        print("Error: El legajo debe tener exactamente 5 números.")
        legajo = input("Legajo (5 dígitos): ")

    if validar_existe_alumno(legajo, alumnos_dicc):
        print(f"El legajo {legajo} ya existe en el archivo alumnos.txt, no se permite su escritura.")
        return  # Sale de la función sin guardar nada

    promedio_txt = input("Nota Promedio (1 a 10): ")
 
    while not promedio_txt.isdigit() or int(promedio_txt) < 1 or int(promedio_txt) > 10:
        print("Error: La nota debe ser un número entero entre 1 y 10.")
        promedio_txt = input("Nota Promedio (1 a 10): ")

    linea = f"{nombre};{apellido};{legajo};{promedio_txt}\n"
    
    with open("alumnos.txt", "a") as archivo:
        archivo.write(linea)

    alumnos_lista.append([nombre, apellido, legajo, promedio_txt])
    alumnos_dicc[legajo] = {
        "nombre": nombre,
        "apellido": apellido,
        "promedio": promedio_txt
    }

    print("¡Alumno agregado con éxito!")


def guardar_aprobados(alumnos_lista):
    with open("aprobados.txt", "w") as archivo:

        for alumno in alumnos_lista:
            
            if float(alumno[3]) >= 6:
                linea = f"{alumno[0]};{alumno[1]};{alumno[2]};{alumno[3]}\n"
                archivo.write(linea)

    print("--- ALUMNOS APROBADOS (aprobados.txt) ---")
    
    with open("aprobados.txt", "r") as archivo:
        for linea in archivo:
            print(linea.strip()) 

            