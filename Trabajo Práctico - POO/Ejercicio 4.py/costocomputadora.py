from componentecpu import ComponenteCPU
from computadora import Computadora


class CostoComputadora:
    def main(self):
        agregarComputadora = input("¿Desea agregar una computadora? (s/n): ").lower()

        while agregarComputadora == "s":
            print("--- Ingrese los datos de la computadora ---")
            marcaComputadora = input("Marca: ")
            modelo = input("Modelo: ")

            computadora = Computadora(marcaComputadora, modelo)

            print("--- Ingrese los componentes ---")
            agregarComponente = "s"

            while agregarComponente == "s":
                componente = input("Componente: ")
                marcaComponente = input("Marca: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                componenteCPU = ComponenteCPU(
                    componente, marcaComponente, cantidad, precio
                )
                computadora.listaComponenteCPU.append(componenteCPU)

                agregarComponente = input("¿Agregar otro componente (s/n)? ").lower()

            print("-----------Computadora----------------")
            print(f"Marca: {marcaComputadora}")
            print(f"Modelo: {modelo}")
            print("Componentes:")
            print("Componente   Marca   Cantidad   Precio X Unidad   SubTotal")

            costoTotal = 0

            for comp in computadora.listaComponenteCPU:
                subtotal = comp.precio * comp.cantidad
                costoTotal += subtotal
                print(
                    f"{comp.componente}   {comp.marca}   {comp.cantidad}   {comp.precio:.2f}   {subtotal:.2f}"
                )

            print(f"Costo Total {costoTotal:.2f}")

            if costoTotal < 50000:
                ganancia = (40 / 100) * costoTotal
                precioVenta = costoTotal + ganancia

            else:
                ganancia = (30 / 100) * costoTotal
                precioVenta = costoTotal + ganancia

            print(
                f"El precio sugerido de venta es {costoTotal:.2f} + {ganancia:.2f} = {precioVenta:.2f}"
            )

            agregarComputadora = input(
                "¿Desea cotizar una nueva computadora? (s/n): "
            ).lower()


if __name__ == "__main__":
    costo = CostoComputadora()
    costo.main()
