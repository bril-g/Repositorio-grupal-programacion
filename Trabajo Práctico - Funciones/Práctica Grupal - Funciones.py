# Ejercicio 1: Funciones puras con parámetros opcionales y keyword arguments
def calcular_factura_final(
        monto_base: float, 
        impuesto: float = 21.0, 
        descuento: float = 0.0, 
        envio_prioritario: float | None = None) -> float:

    # Primero aplicamos el descuento
    subtotal = monto_base * (1 - descuento / 100)

    # Aplicamos el impuesto sobre el monto descontado
    total = subtotal * (1 + impuesto / 100)

    # Si existe un envío prioritario, lo sumamos
    if envio_prioritario is not None:
        total += envio_prioritario

    # Redondeamos el resultado a 2 decimales
    return round(total, 2)

# Pruebas obligatorias
print(calcular_factura_final(1000.0))
print(calcular_factura_final(1000.0, descuento=10.0))
print(calcular_factura_final(1000.0, impuesto=10.0, descuento=5.0, envio_prioritario=150.0))

# Ejercicio 5: Sistema Integrador (POO, Estáticos, Métodos y Kwargs)
class CalculadoraFitness:
    @staticmethod
    def calcular_imc(peso_kg: float, altura_m: float) -> float:
        imc = peso_kg / (altura_m ** 2)
        return imc

    @staticmethod
    def clasificar_nivel(imc: float) -> str:
        if imc < 18.5:
            return "Bajo peso"
        elif imc < 25.0:
            return "Normal"
        else:
            return "Sobrepeso"


class Atleta:
    def __init__(self, nombre: str, peso: float, altura: float):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura

    def obtener_reporte(self, incluir_recomendacion: bool = False, **metricas_extra) -> str:
        reporte = ""

        imc = CalculadoraFitness.calcular_imc(self.peso, self.altura)
        reporte += f"IMC: {imc}" + "\n"

        nivel = CalculadoraFitness.clasificar_nivel(imc)
        reporte += f"Nivel: {nivel}" + "\n"

        for clave, valor in metricas_extra.items():
            reporte += f"{clave}: {valor}" + "\n"

        if incluir_recomendacion:
            if nivel == "Bajo peso":
                reporte += f"Recomendación: aumentar ingesta calórica"
            elif nivel == "Normal":
                reporte += f"Recomendación: mantener el plan actual"
            else:
                reporte += f"Recomendación: consultar a un nutricionista"

        return reporte

atleta = Atleta("Juan", 80, 1.75)
print(atleta.obtener_reporte(incluir_recomendacion = True, ritmo = "5:30/km", frecuencia = 160))
