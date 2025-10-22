#3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
#algoritmo general. 

def potenciar(numero,potencia):
    if potencia==1:
        return numero
    else:
        return numero * potenciar(numero,potencia-1)
    

numero=int(input("ingrese el numero que desea potenciar: "))
potencia=int(input("ingrese la potencia deseada: "))
print (f"la potencia de {numero} elevado a {potencia} es {potenciar(numero,potencia)}")

