with open("alumnosynotas.txt","w") as archivo:
    archivo.write("nombre;apellido;legajo;notapromedio")
    archivo.write("Juan;Pérez;53365;8\n")
    archivo.write("María;López;55654;10\n")
    archivo.write("Pablo;Gómez;58999;6\n")

x="00323984"
try:
    int(x)
    print("x puede convertirse en número")
except ValueError:
    print("x no es numérica")
