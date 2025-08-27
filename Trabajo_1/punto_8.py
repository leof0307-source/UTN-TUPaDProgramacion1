#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
#modo:

peso= float(input("ingrese su peso aqui"))
altura= float(input("ingrese su altura en metrtos"))
IMC= peso/(altura)**2
print (f"su indice de masa corporal es de {IMC}")
