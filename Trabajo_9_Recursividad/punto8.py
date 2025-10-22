def sumar_numero(numero):
    if numero=="":
        return 0
    else:
        return sumar_numero(numero[1:])+ (numero[0])


numero="12345"  
print(sumar_numero(numero))