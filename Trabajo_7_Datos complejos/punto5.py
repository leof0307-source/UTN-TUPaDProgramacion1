#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.
set1=[]
diccionario={}
lista_temporal=[]
frase=input("Ingrese una frase:")
frase=frase.split( )
for i in range (len(frase)):           #como agrego el set aqui si directamente puedo usar el diccionario
    if frase[i] in diccionario:
        diccionario[frase[i]]+=1
    else:
        diccionario[frase[i]]=1
print (diccionario)
