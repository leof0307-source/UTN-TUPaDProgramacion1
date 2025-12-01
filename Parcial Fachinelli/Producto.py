"""Clase Producto 
Atributos: 
Código (numero), denominación (str), rubro(str), marca(str), precioCompra(numero)"""


class producto:
    def __init__(self,codigo,denomin,rub,marc,precioCompra):
        self.codigo=codigo
        self.denominacion=denomin
        self.rubro=rub
        self.marca=marc
        self.precioCompra=float(precioCompra)


        
    