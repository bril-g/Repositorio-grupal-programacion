# --- Ejercicio 1 ---

class Celda:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor


class Matriz:
    def __init__(self):
        self.celdasMatriz = []

    def agregar(self, celda: Celda):
        for c in self.celdasMatriz:
            if c.fila == celda.fila and c.columna == celda.columna:
                print(f"Ya hay un valor en ({celda.fila}, {celda.columna})")
                return
        self.celdasMatriz.append(celda)

    def obtener(self, fila, columna):
        for c in self.celdasMatriz:
            if c.fila == fila and c.columna == columna:
                return c.valor
        return "La fila y columna indicada no ha sido asignada en ninguna celda"


# --- Script principal ---

m = Matriz()

while True:
    valor = input("Ingrese un valor para la celda (ingrese FIN para finalizar): ")
    if valor == "FIN":
        break
    else:
        fila = int(input("Ingrese el n° de la fila donde se desea almacenar el valor: "))
        columna = int(input("Ingrese el n° de la columna donde se desea almacenar el valor: "))
        celda1 = Celda(fila, columna, valor)
        m.agregar(celda1)

# Mostrar celdas cargadas
for c in m.celdasMatriz:
    print(f"({c.fila}, {c.columna}) = {c.valor}")

# Buscar una celda
resultado = m.obtener(1, 1)
print(resultado)   