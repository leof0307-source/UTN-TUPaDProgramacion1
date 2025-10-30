import csv
def validarnumero(numero):
    try:
        int(numero)
        return True
    except ValueError:
        print("el dato no es numérico ingrese datos correctos")
        return False
def mostrar_paises():
    with open ("paises.csv","r") as archivo:
        lector=csv.reader(archivo)
        print (lector)

def limpiar_texto(texto):
    texto = texto.lower()
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    return texto
def pais_existe(nombre_pais):
    nombre_limpio = limpiar_texto(nombre_pais)

    with open("paises.csv", newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if not fila:
                continue
            pais_csv = limpiar_texto(fila[0])
            if pais_csv == nombre_limpio:
                return True
    return False
def agregar_paises():      #nombre,poblacion,superficie,continente
    with open("paises.csv","a",newline="") as archivo:
        while True:
            pais=input ("ingrese el nombre del pais")
            if not pais.isalpha():
                print("ingrese solo etras")
                continue
            else:
                if pais_existe(pais)== True:
                    print("nombre guardado")
                    break
                else:
                    print("el pais ya existe en el archivo, introduzca otro")
                    continue

        while True:
            poblacion=input("ingrese la poblacion del pais sin puntos:")
            poblacion.split(".")
            if validarnumero(poblacion) == True:
                print ("poblacion guardada")
                int(poblacion)
                continue
            else:
                print("no es un numero intentelo de nuevo")
                break

        while True:
            superficie=input("ingrese la superficie de el pais en km2:")
            if validarnumero(superficie) == True:
                print ("superficie guardada")
                int(superficie)
                continue
            else:
                print("no es un numero intentelo de nuevo")
                break
                
        while True:
            continente=input("ingrese el continente al que pertenece")
            if not continente.isalpha():
                print("ingrese solo letras")
                





        escritor = csv.writer(archivo)
        escritor.writerow([nombre, apellido, legajo, nota])

