#cantidad (numero entero), Producto (objeto Producto asociado), subtotal (numero, será calculado 
#precio del producto * cantidad)

class DetalleOrdenCompra:
    def __init__(self,cantidad,producto,subtotal):
        self.cantidad=cantidad
        self.producto=producto
        self.subtotal=subtotal
        