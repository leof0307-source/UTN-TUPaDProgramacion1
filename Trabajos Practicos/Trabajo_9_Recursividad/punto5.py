def es_palindromo(letras):
    if letras=="":
        return ""
    else:
        return es_palindromo(letras[1:])+letras[0]


letras="otto"                                     #Y OTTO ES OTTO ESCRITO AL REVEZ JAJJAJAJA
if letras==es_palindromo(letras):                 #no me asustes
    print ("es palindromo")
else:
    print("no es palindromo")
