class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self._salario = salario

    def mostrar_info(self):
        return f"Empleado: {self.nombre}, Salario: ${self._salario}"

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, nuevo_salario):
        if nuevo_salario >= 0:
            self._salario = nuevo_salario
        else:
            print("Error: salario no puede ser negativo.")

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def mostrar_info(self):
        return f"Gerente: {self.nombre}, Dpto: {self.departamento}, Salario: ${self.salario}"

# Ejemplo
empleado = Empleado("Carlos", 2500)
empleado.salario = 2700
print(empleado.mostrar_info())

gerente = Gerente("Ana", 5000, "Ventas")
print(gerente.mostrar_info())