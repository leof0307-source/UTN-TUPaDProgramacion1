"""Clase DetalleFactura 
Atributos: 
cantidad (numero entero), articulo (objeto Articulo asociado), subtotal (numero, será calculado 
precio * cantidad)"""
class dertallefaactura:
    def __init__(self,cantidad,articulo,subtotal):
        self.cantidad=cantidad
        self.articulo=articulo
        self.subtotal= cantidad * subtotal