# b) atributos privados y protegidos
class Coche:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.__modelo = modelo          # atributo privado
        self._velocidad_maxima = velocidad_maxima  # protegido

    def mostrar_modelo(self):
        print(f"El modelo es {self.__modelo}")

# Ejemplo
mi_coche = Coche("Toyota", "Corolla", 180)
mi_coche.mostrar_modelo()