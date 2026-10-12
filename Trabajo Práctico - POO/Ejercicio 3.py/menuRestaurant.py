from ingrediente import Ingrediente
from plato import Plato


class MenuRestaurant:
    def main(self):
        platosMenu = []

        agregarPlato = input("¿Desea agregar un plato? (s/n): ").lower()
        while agregarPlato == "s":
            print("--- Ingrese los datos del plato ---")
            nombreCompleto = input("Nombre completo: ")
            precio = float(input("Precio: "))
            esBebida = input("¿Es bebida? (s/n): ").lower() == "s"

            plato = Plato(nombreCompleto, precio, esBebida)

            if not esBebida:
                print("--- Ingrese los ingredientes del plato ---")
                agregarIngrediente = "s"
                while agregarIngrediente == "s":
                    nombre = input("Nombre: ")
                    cantidad = float(input("Cantidad: "))
                    unidadMedida = input("Unidad de medida: ")

                    ingrediente = Ingrediente(nombre, cantidad, unidadMedida)
                    plato.listaIngredientes.append(ingrediente)

                    agregarIngrediente = input(
                        "¿Agregar otro ingrediente? (s/n): "
                    ).lower()

            platosMenu.append(plato)
            agregarPlato = input("¿Desea agregar otro plato? (s/n): ").lower()

        self.mostrarMenu(platosMenu)

    def mostrarMenu(self, platosMenu):
        print("-----------MENÚ----------------")
        for plato in platosMenu:
            print(plato.nombreCompleto)
            print(f"Precio: $ {plato.precio:.2f}")
            if not plato.esBebida:
                print("Ingredientes:")
                print("Nombre   Cantidad   Unidad de Medida")
                for ing in plato.listaIngredientes:
                    print(f"{ing.nombre}   {ing.cantidad:.2f}   {ing.unidadMedida}")
            print("----------------------------------")


if __name__ == "__main__":
    menu = MenuRestaurant()
    menu.main()
