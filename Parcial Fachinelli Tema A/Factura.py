"""Clase Factura 
Atributos: 
fecha (día de hoy), numero (autogenerado iniciando en 1), total (será calculado por la suma de los 
detalles), listaDetalles (lista de objetos DetalleFactura) """
class factura:
    def __init__(self,dia,numero,total,listadetalles):
        self.dia=dia
        self.numero=numero
        self.total=total
        self.listadetalles=listadetalles

    def agregarDetalle(self,detalle):
        self.listadetalles.append(detalle)
        self.total =+ detalle.precioVenta   #error importante, 
    
        
