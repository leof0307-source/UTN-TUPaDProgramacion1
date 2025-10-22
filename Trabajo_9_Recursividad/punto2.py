#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
#especifique. 
def fibonacci(numero):
    if numero==1:
        return 1
    elif numero==0:
        return 0
    else:
        return fibonacci(numero-1)+fibonacci(numero-2)
    
numero=int(input("ingrese el numero para calcular su fibonacci: "))
numero1=int(input("ingrese el numero desde donde calcular su fibonacci: "))
for numero1 in range (1,numero + 1):
    print (fibonacci(numero1))
    print("__________")
