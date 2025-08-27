#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
#su perímetro. 

radio=float(input("ingrese el radio del circulo en centimetros"))
area= 3.14 * radio ** 2
perimetro= 2 * 3.14 * radio
print(f"el area del circulo es {area} y su perimetro es {perimetro}")