contador_positivos=0
contador_negativos=0
contador_pares=0
contador_impares=0
contador_ceros=0  #aqui agrego una categoria ya que 0 no entra en las categorias anteriores
for i in range (6):
    numero=float(input("ingrese un numero"))
    if numero==0:
        contador_ceros +=1
    elif numero >0:
        contador_positivos +=1
    elif numero <0:
        contador_negativos +=1
    elif numero %2==0:
        contador_pares +=1
    elif numero %2 !=0:
        contador_impares +=1
print("la cantidad de numeros positivos es=", + contador_positivos)
print("la cantidad de numeros negativos es=", + contador_negativos)
print("la cantidad de numeros pares es=", + contador_pares)
print("la cantidad de numeros impares es=", + contador_impares)