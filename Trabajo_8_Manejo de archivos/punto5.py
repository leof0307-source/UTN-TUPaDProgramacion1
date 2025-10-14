#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
#no existe, mostrar un mensaje de error.
partes=[]
productos=[]
i=0
with open("productos2.txt","r") as archivo:
    for linea in archivo:
        partes.append(linea.strip().split(","))
        productos.append({
            "fruta":partes[i][0],
            "precio":partes[i][1],
            "cantidad":partes[i][2]
        })
        i+=1

fruta=input("ingrese la fruta para consultar su existencia: ")
bandera=False
fruta=fruta.lower()
for j in range(len(productos)):
    if fruta==productos[j]["fruta"]:
        print (productos[j])
        bandera=True
        break
    else:
        bandera=False

if bandera==False:
    print("error")
