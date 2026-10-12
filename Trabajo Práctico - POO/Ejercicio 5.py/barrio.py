class Barrio:
    def __init__(self, nombre, empresaConstructora):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.vivienda = []

    def getSuperficieTotalTerreno(self):
        superficieTotal = 0

        for objeto in self.vivienda:
            superficieTotal += objeto.superficieTerreno

        return superficieTotal

    def getSuperficieTotalTerrenoXManzana(self, manzana):
        superficieTotalXManzana = 0

        for objeto in self.vivienda:
            if objeto.manzana == manzana:
                superficieTotalXManzana += objeto.superficieTerreno

        return superficieTotalXManzana

    def getSuperficieTotalCubierta(self):
        superficieTotalCubierta = 0

        for objeto in self.vivienda:
            superficieTotalCubierta += objeto.getMetrosCuadradosCubiertos()

        return superficieTotalCubierta
