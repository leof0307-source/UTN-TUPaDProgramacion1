#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.
productos={"manzanas":50, "naranjas":30, "peras":20}
while True:
    print("\nOpciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades al stock de un producto existente")
    print("3. Agregar un nuevo producto")
    print("4. Salir")
    opcion=input("Seleccione una opción (1-4):")
    
    if opcion=="1":
        producto=input("Ingrese el nombre del producto a consultar:")
        if producto in productos:
            print(f"El stock de {producto} es {productos[producto]}")
        else:
            print(f"El producto {producto} no existe en el inventario.")
    
    elif opcion=="2":
        producto=input("Ingrese el nombre del producto al que desea agregar stock:")
        if producto in productos:
            try:
                cantidad=int(input(f"Ingrese la cantidad de unidades a agregar a {producto}:"))
                if cantidad > 0:
                    productos[producto] += cantidad
                    print(f"Nuevo stock de {producto} es {productos[producto]}")
                else:
                    print("La cantidad debe ser un número positivo.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        else:
            print(f"El producto {producto} no existe en el inventario.")
    
    elif opcion=="3":
        producto=input("Ingrese el nombre del nuevo producto:")
        if producto in productos:
            print(f"El producto {producto} ya existe en el inventario con stock {productos[producto]}.")
        else:
            try:
                cantidad=int(input(f"Ingrese la cantidad inicial de unidades para {producto}:"))
                if cantidad >= 0:
                    productos[producto] = cantidad
                    print(f"Producto {producto} agregado con stock {cantidad}.")
                else:
                    print("La cantidad debe ser un número no negativo.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
    
    elif opcion=="4":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.")