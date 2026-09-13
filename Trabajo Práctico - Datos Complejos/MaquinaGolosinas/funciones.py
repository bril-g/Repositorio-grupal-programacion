def mostrarGolosinas(golosinas):

    print("Código | Golosina | Stock")
    print("--------------------------")

    for fila in golosinas:
        print(f"{fila[0]} | {fila[1]} | {fila[2]}")

def pedirGolosina(empleados, golosinas, golosinasPedidas):
    legajoEmpleado = int(input("Ingrese n° de legajo: "))

    if legajoEmpleado in empleados:

        codigoGolosina = int(input("Ingrese el código de la golosina: "))

        encontradaGolosina = False

        for fila in golosinas:

            if fila[0] == codigoGolosina:

                encontradaGolosina = True

                if fila[2] > 0:

                    fila[2] -= 1

                    codigo = fila[0]
                    denominacion = fila[1]

                    encontradaPedido = False

                    for fila in golosinasPedidas:

                        if fila[0] == codigoGolosina:
                            fila[2] += 1
                            encontradaPedido = True

                    if encontradaPedido == False:
                        nuevaFila = [codigo, denominacion, 1]
                        golosinasPedidas.append(nuevaFila)

                else:
                    print(f"Lo sentimos, la golosina {fila[1]} no se encuentra disponible, seleccione otra golosina o ingrese salir.")

        if encontradaGolosina == False:
            print("El código de la golosina no es válido.")

    else:
        print("Usted no es empleado de la empresa.")

def rellenarGolosinas(clavesTecnico, golosinas):
    clave1 = input("Ingresa la primera clave: ")
    clave2 = input("Ingresa la segunda clave: ")
    clave3 = input("Ingresa la tercera clave: ")

    if (clave1, clave2, clave3) == clavesTecnico:

        codigoGolosina = int(input("Ingrese el código de la golosina: "))

        encontradaGolosina = False

        for fila in golosinas:

            if fila[0] == codigoGolosina:

                cantidadRecargar = int(input("Ingrese la cantidad a recargar: "))

                encontradaGolosina = True

                if cantidadRecargar > 0:
                    fila[2] += cantidadRecargar

                else:
                    print("Ingrese una cantidad mayor a 0.")

        if encontradaGolosina == False:
            print("El código de la golosina no es válido.")

    else:
        print("No tiene permiso para ejecutar la función de recarga.")

def apagarMaquina(golosinasPedidas):
    print(golosinasPedidas)

    SumaGolosinas = 0

    for fila in golosinasPedidas:
        SumaGolosinas += fila[2]

    print(SumaGolosinas)