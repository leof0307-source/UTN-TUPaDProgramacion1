class rectangulo:
    def __init__(self,altura,base):
        self.base=base
        self.altura=altura

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2*(self.base + self.altura)
    
r1=rectangulo(5,3)
print(r1.area())
print (r1.perimetro())

