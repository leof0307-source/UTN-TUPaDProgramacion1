from nota import Nota

class Alumno:
    def __init__(self, nombreCompleto, legajo):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0
        suma = 0
        for n in self.notas:
            suma += n.notaExamen
        return suma / len(self.notas)
