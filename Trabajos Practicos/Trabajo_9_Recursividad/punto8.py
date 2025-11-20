def contar_digito(numero, digito):
    # Caso base: si ya no quedan más dígitos
    if numero == 0:
        return 0
    
    # Contar si el último dígito coincide
    ultimo = numero % 10
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)