def agregardiccionario(alumnos):
    with open("alumnosynotas.txt","r") as archivo:
        for linea in archivo:
            partes=linea.strip().split(",")
            nombre=partes[0]
            apellido=partes[1]
            legajo=partes[2]
            nota=partes[3]
            valor = (f"{nombre},{apellido},{nota}")
            clave=legajo
            alumnos[clave]=valor
    return alumnos


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
alumnos=[]
with open("alumnosynotas.txt","r") as archivo:
    for linea in archivo:
        partes=linea.strip().split(",")
        nombre=partes[0]
        apellido=partes[1]
        legajo=partes[2]
        nota=partes[3]
        valor = (f"{nombre},{apellido},{nota}")
        clave=legajo
        alumnos[clave]=valor     