#1. Crear archivo inicial con productos: Crear un archivo de texto llamado
#productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

with open("productos.txt","w") as archivo:
    archivo.write("lapices,1.500,20\n")
    archivo.write("Blocks,8.000,10\n")
    archivo.write("resaltadores,2.000,30\n")

