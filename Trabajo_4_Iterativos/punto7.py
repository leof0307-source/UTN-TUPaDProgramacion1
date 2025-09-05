sumatoria=0
numero=int(input("ingrese un numero al que quiere summar desde 0:"))
if numero >0:
    for i in range (0,numero+1):
        sumatoria +=i
        print(sumatoria)
else:
    print("ingrese un numero entero positivo")