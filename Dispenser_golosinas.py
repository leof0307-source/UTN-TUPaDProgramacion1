
encendida=True
productos = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 11],
    [15, "Lata Coca", 12],
    [20, "Chitos", 10]
]
empleados = {
    "1100":"José Alonso",
    "1200":"Federico",
    "1300":"Nelson Pereira",
    "1400":"Osvaldo Tejada",
    "1500":"Gastón Garcia "
    }
clavesTecnico=("admin","CCCDDD","2020")

golosinas_pedidas=[]

while encendida:
    opcion=input("Ingrese una opción:""1:pedir golosinas "
    "2:agregar golosinas "
    "3:mostrar golosinas "
    "4:apagar la maquina ")
    if opcion=="1":
        cedula=input("Ingrese su cédula:")
        if cedula in empleados:
            print("Bienvenido a la máquina expendedora")
            for i in range(len(productos)):
                print(f"{productos[i][0]}: {productos[i][1]} - Stock: {productos[i][2]}")
            
            eleccion=int(input("Ingrese el número del producto que desea:"))    #aca como hago para verificar que la eleccion esta en el rango de productos
            encontrado = False
            for i in range(len(productos)):
                if productos[i][0] == eleccion:
                    indice_producto = i
                    encontrado = True
                    break
                    indice_producto = -1
            if encontrado:
                nombre=productos[indice_producto][1] #como hago para volver a la instruccion anterior
                
                if productos[indice_producto][2]>0:
                    productos[indice_producto][2] -= 1
                    encontrado = False
                    print(f"producto entregado. Stock restante: {productos[indice_producto][2]}")
                    for i in range(len(golosinas_pedidas)):
                        if golosinas_pedidas[i][1] == nombre:
                            golosinas_pedidas[i][2] += 1
                            encontrado = True
                            break
                    
                    if not encontrado:
                        golosinas_pedidas.append([indice_producto,nombre, 1])
                else:
                    print("producto agotado.")
            else:
                print("El producto seleccionado no existe.")

        else :
            print("usted no es un empleado de la empresa")
    
    elif opcion=="2":
        usuario=input("Ingrese su usuario:")
        contrasena=input("Ingrese su contraseña:")
        codigoNumerico=input("Ingrese el código numérico:")
        if (usuario, contrasena, codigoNumerico) == clavesTecnico:
            print("Bienvenido técnico autorizado")

            for i in range(len(productos)):
                print(f"{productos[i][0]}: {productos[i][1]} - Stock: {productos[i][2]}")
            eleccion=int(input("Ingrese el número del producto que desea reponer:"))
            cantidad=int(input("Ingrese la cantidad que desea agregar:"))
            for i in range(len(productos)):
                for j in range(len(productos[i])):
                    ubicacion=productos[i][0]
                    if ubicacion == eleccion :
                        productos[i][2] += cantidad
                        print(f"Stock actualizado. Nuevo stock de {productos[i][1]}: {productos[i][2]}")
                        break

        else:
            print("“No tiene permiso para ejecutar la función de recarga")

    elif opcion=="3":
        print("Productos:")
        for i in range(len(productos)):
            print(f"{productos[i][0]}: {productos[i][1]} - Stock: {productos[i][2]}")

    elif opcion=="4":
        print("apagando la máquina...")
        for i in range(len(golosinas_pedidas)):
            print(f"{golosinas_pedidas[i][0]}: {golosinas_pedidas[i][1]} - Cantidad pedida: {golosinas_pedidas[i][2]}")
        encendida=False
    else:
        print("Opción no válida, intente de nuevo.")