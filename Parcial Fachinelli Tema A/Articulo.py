"""Clase Articulo 
Atributos: 
Código (numero), denominación (str), rubro(str), marca(str), precioVenta(numero)"""

class articulo:
    def __init__(self,codigo,denominacion,rubro,marca,precioVenta):
        self.codigo=codigo
        self.denominacion=denominacion
        self.rubro=rubro
        self.marca=marca
        precioVenta=int(precioVenta)