from datos import *
from funciones import *

while True:

    print("1. Pedir golosinas.")
    print("2. Mostrar golosinas.")
    print("3. Rellenar golosinas.")
    print("4. Apagar máquina.")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        pedirGolosina(empleados, golosinas, golosinasPedidas)

    if opcion == 2:
        mostrarGolosinas(golosinas)

    if opcion == 3:
        rellenarGolosinas(clavesTecnico, golosinas)

    if opcion == 4:
        apagarMaquina(golosinasPedidas)
        break