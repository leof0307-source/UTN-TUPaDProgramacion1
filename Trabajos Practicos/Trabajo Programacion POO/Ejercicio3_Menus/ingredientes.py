class Ingrediente:
    def __init__(self,nombre,cantidad,unidaddemedida):
        self.nombre=nombre
        self.cantidad=cantidad
        self.unidaddemedida=unidaddemedida
    def __str__(self):
        return f"{self.nombre}: {self.cantidad} {self.unidaddemedida}"