#4) Crear una función recursiva en Python que reciba un número entero positivo en base 
#decimal y devuelva su representación en binario como una cadena de texto. 

def convertir_binario(numero):
    if numero==0:
        return "0" 
    elif numero==1:
        return "1"
    else:
        return (convertir_binario(numero//2))+str(numero%2)


print(convertir_binario(10))

