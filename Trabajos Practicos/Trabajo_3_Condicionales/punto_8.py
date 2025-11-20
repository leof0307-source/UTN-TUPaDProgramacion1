nombre=input("ingrese el nombre ")
numero=input("ingrese 1 para mayusculas,2 para minusculas y 3 para la primera en mayuscula")

if numero=="1":
    nombre2=nombre.upper()
    print(nombre2)
elif numero=="2":
    nombre2=nombre.lower()
    print(nombre2)
elif numero=="3":
    nombre2=nombre.title()
    print(nombre2)
    