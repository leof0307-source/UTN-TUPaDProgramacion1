"""Clase OrdenCompra 
Atributos: 
fecha (día de hoy), numero (autogenerado iniciando en 1), total (será calculado por la suma de los 
subtotales de los detalles), listaDetalles (lista de objetos DetalleOrdenCompra) """
"""from datetime import date 
#Día actual 
fechaHoy = date.today() 
print(fechaHoy)"""

class ordencompra:
    def __init__(self, fecha, numero,listaDetalles):
        self.fecha = fecha
        self.numero = numero
        self.total = 0
        self.listaDetalles = [] 

    def agregar_detalle(self, detalle):
        self.listaDetalles.append(detalle)
        self.total += detalle.subtotal