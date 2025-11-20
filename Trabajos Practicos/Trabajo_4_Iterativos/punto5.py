import random
contador=0
numero=int(input("ingrese un numero:"))
numero_adivinar=random.randint(0,9)
if numero==numero_adivinar:
    print("lo lograste al primer intento,bien hecho")
else:
    contador +=1

while numero!=numero_adivinar:
    print("intenta de nuevo")
    numero=int(input("ingrese el numero"))
    contador+=1
    if numero==numero_adivinar:
        print(f"lo lograste en el intento {contador},bien hecho")
    