#fecha (día de hoy), numero (autogenerado iniciando en 1), total (será calculado por la suma de los 
#subtotales de los detalles), listaDetalles (lista de objetos DetalleOrdenCompra)
class OrdenCompra:
    def __init__(self,fecha,numero,total,listaDetalles):
        self.fecha=fecha
        self.numero=numero
        self.total=total
        self.listaDetalles=listaDetalles