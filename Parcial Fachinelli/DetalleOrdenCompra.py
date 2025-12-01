"""Clase DetalleOrdenCompra 
Atributos: 
cantidad (numero entero), Producto (objeto Producto asociado), subtotal (numero, será calculado 
precio del producto * cantidad)"""
class detalleordencompra:
    def __init__(self,cantidad,producto,subtotal):
        self.cantidad=cantidad
        self.producto=producto
        self.subtotal=subtotal * cantidad
