# h) Asociación: Una clase "Persona" puede tener una relación de asociación con una clase "Coche", donde una persona puede poseer un coche, pero el coche puede existir independientemente de la persona.
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.coche = None

    def asignar_coche(self, coche):
        self.coche = coche

    def mostrar_info(self):
        if self.coche:
            print(f"{self.nombre} tiene un coche {self.coche.marca} {self.coche.modelo}.")
        else:
            print(f"{self.nombre} no tiene coche.")

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# Ejemplo
persona = Persona("Carlos")
auto = Coche("Toyota", "Corolla")
persona.asignar_coche(auto)
persona.mostrar_info()