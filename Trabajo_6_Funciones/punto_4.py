#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
#dio como parámetro y devuelva el área del círculo. calcular_peri
#metro_circulo(radio) que reciba el radio como parámetro y devuel
#va el perímetro del círculo. Solicitar el radio al usuario y llamar am
#bas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    return 3.14 * radio ** 2
def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio

radio=float(input("ingrese el radio del circulo: "))
print(f"el area del circulo es: {calcular_area_circulo(radio)}")
print(f"el perimetro del circulo es: {calcular_perimetro_circulo(radio)}")
