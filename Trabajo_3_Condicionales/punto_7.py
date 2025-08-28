palabra=input("ingrese su palabra ")

ultima_letra=palabra[-1]
if ultima_letra==("a" or "e" or "i" or "o" or "u"):
    print(palabra + "!")
else:
    print(palabra)
    