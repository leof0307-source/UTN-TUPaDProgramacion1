#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.
contactos={}
for i in range(2):
    nombre=input("Ingrese el nombre del contacto:")
    nombre=nombre.upper()
    numero=input("Ingrese el número del contacto:")
    contactos[nombre]=numero
respuesta=input("¿desea revisar su lista de contactos? (s/n):")
if respuesta.lower()=="s":
    for i in range(2):
        consulta=input("Ingrese el nombre del contacto que desea consultar:")
        if consulta in contactos:
            print(f"El número de {consulta} es {contactos[consulta]}")
        else:
            print(f"El contacto {consulta} no se encuentra en la lista")


