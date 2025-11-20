import csv

def leer_parte(pais,numero,dato):
    if pais_existe(pais):
        aux=limpiar_texto(pais)
        with open("paises.csv", "r") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if fila[0]==aux:
                    print(f"el{dato} del pais {aux} es de {fila[int(numero)]}")

def validarnumero(numero):
    try:
        int(numero)
        return True
    except ValueError:
        print("el dato no es numérico ingrese datos correctos")
        return False
    
def mostrar_paises():
    with open("paises.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            print(fila)


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

def agregar_paises(tupla_continentes):      #nombre,poblacion,superficie,continente
    with open("paises.csv","a",newline=",",encoding="utf-8") as archivo:
        while True:
            pais=input ("ingrese el nombre del pais")
            if not pais.isalpha():
                print("ingrese solo etras")
                continue
            else:
                if pais_existe(pais)== False:
                    print("pais guardado")
                    break
                else:
                    print("el pais ya existe en el archivo, introduzca otro")
                    continue

        while True:
            poblacion=input("ingrese la poblacion del pais sin puntos:")
            poblacion = poblacion.replace(".", "")
            if validarnumero(poblacion) == True:
                print ("poblacion guardada")
                int(poblacion)
                break
            else:
                print("no es un numero intentelo de nuevo")
                continue

        while True:
            superficie=input("ingrese la superficie de el pais en km2:")
            if validarnumero(superficie) == True:
                print ("superficie guardada")
                int(superficie)
                break
            else:
                print("no es un numero intentelo de nuevo")
                continue
                
        while True:
            continente=input("ingrese el continente al que pertenece: ")
            if not continente.isalpha():
                print("ingrese solo letras")
                continue
            else:
                if limpiar_texto(continente) in tupla_continentes:
                    print("el continente se guardo correctamente")
                    break
                else:
                    print("ese continente no existe intente de nuevo")

        escritor = csv.writer(archivo)
        escritor.writerow([pais, poblacion, superficie, continente])

#################################################################PRINCIPAL############################################################################

tupla_continentes = ("africa", "america", "antartida", "asia", "europa", "oceania")
partes={"1":"poblacion","2":"superficie","3":"continente"}
while True:
    eleccion=input("ingrese que desea hacer" \
    "1:leer archivo " \
    "2:agregar pais " \
    "3:ver info especifica " \
    "4:salir ")
    if eleccion=="1":
        mostrar_paises()
    elif eleccion== "2":
        agregar_paises(tupla_continentes)
    elif eleccion=="3":
        pais_a_saber=input("ingrese el pais para ver su info: ")
        if pais_existe(pais_a_saber):
            while True:
                dato=input("que desea ver? " \
                "1:poblacion " \
                "2:superficie " \
                "3:continente ")
                if dato=="1" or dato=="2" or dato=="3":
                    leer_parte(pais_a_saber,int(dato),partes[dato])              #cuidado en como se pasan los parametros 
                    break
                else:
                    print("ingrese una opcion valida")
                    continue
        else:
            print("ese pais no existe o necesita agregarlo")
            continue

