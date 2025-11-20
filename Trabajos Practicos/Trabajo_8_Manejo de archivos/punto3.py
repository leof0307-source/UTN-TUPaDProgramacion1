#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente.

with open("productos.txt","w") as archivo:
    archivo.write("lapices,1.500,20\n")
    archivo.write("Blocks,8.000,10\n")
    archivo.write("resaltadores,2.000,30\n")

with open("productos.txt","r") as archivo:
    leer=archivo.read()
    print(leer)

with open("productos.txt","a") as archivo:
    producto=input("ingrese el producto,precio y cantidad separado por comas")
    archivo.write(producto)