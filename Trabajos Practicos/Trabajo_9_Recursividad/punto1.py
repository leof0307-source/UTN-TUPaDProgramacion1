#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
#función para calcular y mostrar en pantalla el factorial de todos los números enteros 
#entre 1 y el número que indique el usuario 

def fibonacci(numero):
    if numero==1:
        return 1
    elif numero==0:
        return 0
    else:
        return fibonacci(numero-1)+fibonacci(numero-2)
    
numero=int(input("ingrese el numero para calcular su fibonacci: "))
    
for i in range (1,numero + 1):
    print (fibonacci(i))
    print("__________")
