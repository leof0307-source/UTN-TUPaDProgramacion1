class Computadora:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.componentesCPU = []


    def agregar_componente(self, componente):
        self.componentesCPU.append(componente)

    def costo_total(self):
        total = 0

        for c in self.componentesCPU:
            total += c.cantidad * c.precio
        return total
    
    def precio_venta_sugerido(self):
        costo = self.costo_total()

        if costo <= 50000:
            precioSugerido = costo + (costo * 0.4)
        elif costo > 50000:
            precioSugerido = costo + (costo * 0.3)

        return precioSugerido