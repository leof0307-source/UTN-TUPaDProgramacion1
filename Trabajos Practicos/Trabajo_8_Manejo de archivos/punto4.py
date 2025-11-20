#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
#una lista llamada productos, donde cada elemento sea un diccionario con claves: 
#nombre, precio, cantidad.
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
print (productos)
         
          
            



