class Vivienda:
    def __init__(self, calle, numero, manzana, nroCasa, superficieTerreno):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitacion = []

    def getMetrosCuadradosCubiertos(self):
        metrosCuadradosCubiertos = 0

        for objeto in self.habitacion:
            metrosCuadradosCubiertos += objeto.metrosCuadrados

        if metrosCuadradosCubiertos > self.superficieTerreno:
            print(
                "La superficie cubierta no puede ser mayor a la superficie del terreno."
            )

        return metrosCuadradosCubiertos
