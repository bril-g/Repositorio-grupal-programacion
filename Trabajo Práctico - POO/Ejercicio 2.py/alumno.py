class Alumno:
    def __init__(self, nombreCompleto, legajo):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = []

    def promedio(self):
        total = 0
        for nota in self.notas:
            total = total + nota.notaExamen
        return total / len(self.notas)

    def __str__(self):
        return f"{self.nombreCompleto} - Legajo: {self.legajo}"
    