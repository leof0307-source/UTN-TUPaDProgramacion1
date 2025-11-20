class saludar:
    def __init__(self,nombre,años):
        self.nombre=nombre
        self.años=años

    def saludar(self):
        print(f"hola {self.nombre} tienes {self.años}")

persona1=saludar("leo",18)
persona1.saludar()
    