import csv

def mostrar_paises():
    with open ("paises.csv","r") as archivo:
        lector=csv.reader(archivo)
        print (lector)

def agregar_paises():