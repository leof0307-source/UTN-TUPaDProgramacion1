#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius=float(input("ingrese la temperatura en grados celsius: "))
print (f"la temperatura en grados fahrenheit es: {celsius_a_fahrenheit(celsius)}")
