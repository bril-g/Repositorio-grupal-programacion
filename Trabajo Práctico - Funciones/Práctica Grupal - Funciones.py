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

# Ejercicio 2: Métodos Estáticos (@staticmethod) como Librería de Utilidades
class ValidadorFinanciero:

    @staticmethod
    def es_cuit_valido(cuit: str) -> bool:
        return len(cuit) == 11 and cuit.isdigit()
    
    @staticmethod
    def convertir_moneda(monto: float, tasa_cambio: float,comision: float = 0.02) -> float:
        monto_convertido = monto * tasa_cambio
        monto_final = monto_convertido * (1 - comision)
        return monto_final

print(ValidadorFinanciero.es_cuit_valido("20384920194")) 
print(ValidadorFinanciero.es_cuit_valido("20-3849201-94")) 
print(ValidadorFinanciero.convertir_moneda(100.0, 1000.0, comision=0.05))

# Ejercicio 3: Interacción Inter-Clase, Métodos de Instancia y Delegación
class Notificador:
    def enviar_recibo(self, cliente: str, total: float) -> None:
        print(f"Enviando recibo a {cliente} por un total de: ${total}")
              
class ProcesadorPagos:
    def __init__(self, notificador: Notificador | None = None):
        if notificador is None:
                 self.notificador = Notificador()
        else:
                 self.notificador = notificador

    def procesar_transaccion(self, cliente: str, items: list[dict],descuento_cupon: float = 0.0) -> float:
        
        subtotal = 0.0
        for product in items:
            subtotal += product["precio"]

        total_final = subtotal - descuento_cupon

        self.notificador.enviar_recibo(cliente, total_final)

        return total_final

carrito = [{"nombre": "Teclado", "precio": 50.0}, {"nombre": "Mouse", "precio": 30.0}]
procesador = ProcesadorPagos()
procesador.procesar_transaccion("Ana Gómez", carrito, descuento_cupon=10.0)

# Ejercicio 4: Manejo de Aridad Variable (*args y **kwargs)
def generar_auditoria_sistema(modulo: str, *mensajes: str, **metadatos) -> str:
    modulo = modulo.upper()

    reporte = ""
    contador = 1

    for mensaje in mensajes:
        reporte += f"[{contador}] {mensaje}" + "\n"
        contador += 1

    for clave, valor in metadatos.items():
        reporte += f"{clave}: {valor}"

    return reporte

log = generar_auditoria_sistema("AUTH", "Intento fallido", "Bloqueo de IP",
usuario="admin", ip="192.168.1.10")

print(log)

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
