
from Producto import producto
from DetalleOrdenCompra import detalleordencompra
from OrdenCompra import ordencompra
from datetime import date
"""Funcionalidades:  
Crear una clase GenerarOrdenComprasMain.py que deberá tener 4 opciones:  
a- Ver Orden de Compras Cargadas 
b- Cargar 1 o más Órdenes de Compra 
c- Generar Archivo Orden de Compra por numero 
d- Salir 
El programa deberá poder: 
"""

#leer archivo

#meter el producto hecho con una clave en el diccionario
"""Opciones del menú:"""

#esqueleto de menu 4 opciones
def menu(ProductosDataBase,OrdenesDeCompra):
    print("1-ver orden archivo orden compra") 
    print("2- generar orden de compra") 
    print("3- generar archivo de orden de compra") 
    print("4-salir")
    while True:
        eleccion=(input("ingerese su eleccion aqui: "))
        if eleccion=="1":
            verordencompra()
        elif eleccion=="2":
            cargarordencompra(ProductosDataBase,OrdenesDeCompra)
        elif eleccion=="3":
            Generararchivo(OrdenesDeCompra)
        elif eleccion=="4":
            print("saliendoo")
        else:
            print("introduzca una opcion valida")
            continue

"""a- Ver Orden de Compras Cargadas: 
- Si se selecciona esta opción se deberá mostrar una lista de las Ordenes de Compra 
cargadas hasta el momento mostrando solo fecha, numero de Orden de Compra y total"""
def verordencompra():
    with open("OrdenesCompras.txt","r") as f:
        lineas = f.readlines()
        if not lineas:
            print("No hay ninguna orden de compra")
        else:
            for linea in lineas:
                print(linea.strip())
"""b- Cargar 1 o más Ordenes de Compras 
- Para esta opción del menú se deberá crear una OrdenCompra asignar sus atributos y 
cargar su detalle correspondiente. Para la carga del detalle se deberá solicitar el código 
del producto a cargar y obtenerlo del diccionario ProductosDataBase, en caso de que el 
código no exista, indicarlo por pantalla y solicitarlo nuevamente. Se deberán cargar 
tantos detalles como se deseen hasta que el usuario indique que no quiere continuar. 
Valide que la cantidad de productos ingresada sea mayor a 0. Validar que se ingrese al 
menos 1 DetalleOrdenCompra. 
- Finalizada la carga de la Orden de Compra guardarla en una variable listaOrdenCompras[] 
y preguntarle al usuario si quiere cargar una nueva Orden de Compra. 
- Si indica que SI deberá repetir el proceso para una nueva orden de compra"""
def mostrar_productos(productosdatabase):
    print("\n--- LISTA DE PRODUCTOS ---")
    print("Código | Denominación | Rubro | Marca | Precio")
    for codigo, producto in productosdatabase.items():
        print(f"{codigo} | {producto.denominacion} | {producto.rubro} | {producto.marca} | {producto.precioCompra}")
def cargarordencompra(productosdatabase,OrdenesDeCompra):
    nummerodeorden=input("ingrese el numero de orden de compra")
    mostrar_productos(productosdatabase)
    while True:
        cod=input("ingrese el codigo del producto")
        if cod in productosdatabase:
            fechaHoy = date.today()
            numero=input("ingrese el numero de la orden")
            orden=ordencompra(fechaHoy,numero,[])
            while True:
                cantidad=int(input("ingrese la cantidad"))
                producto=productosdatabase[cod]
                precio = productosdatabase[cod].precioCompra
                detalle=detalleordencompra(cantidad,producto,precio)
                orden.agregar_detalle(detalle)
                eleccion=input("desea agregar otra orden de compra? s/n")
                eleccion=eleccion.lower()
                if eleccion=="s":
                    print("empezando de nuevo...")
                    continue
                else:
                    print("terminando orden...")
                    OrdenesDeCompra[numero]=orden
                    break
        else:
            print("ingrese una clave existente")
            continue

"""c- Generar Archivo Orden de Compra por numero 
- Solicitar al usuario que ingrese un numero de Orden de Compra; buscar la Orden de 
Compra por su número en la listaOrdenCompras[], si el número de Orden de Compra no 
existe emitir el mensaje “La Orden de Compra con número XXXX no existe”. 
- Si la Orden de Compra existe mostrarla por pantalla con el siguiente formato 
  
Orden de Compra N° XXXXX 
Fecha: XXXXX 
------------ Productos Comprados ------------------------ 
Código  Denominación  Rubro   Marca   Cantidad SubTotal 
XXXXXX XXXXXX  XXXXXX XXXXXX XXXXXX XXXXXX  
 
         TOTAL: XXXXXX 
- Finalmente después de mostrar la Orden de Compra por pantalla preguntar al usuario. 
¿Desea Generar el archivo de la Ordende Compra? Ingrese S para generar u otro carácter 
sino lo desea. 
Si el usuario ingresa S genere un archivo txt llamado ordenCompra_nro_XXXXX.txt con un 
formato lo similar posible al mostrado por pantalla. 
 """
def Generararchivo(OrdenesDeCompra):
    numero = input("Ingrese el número de orden de compra: ")
    
    if numero not in OrdenesDeCompra:
        print(f"La Orden de Compra con número {numero} no existe")
        return

    # Obtener la orden
    orden = OrdenesDeCompra[numero]

    # Mostrar en pantalla
    print(f"\nOrden de Compra N° {orden.numero}")
    print(f"Fecha: {orden.fecha}")
    print("------------ Productos Comprados ------------------------")
    print("Código  Denominación  Rubro   Marca   Cantidad SubTotal")
    
    total = 0
    for detalle in orden.detalles:
        p = detalle.producto
        subtotal = detalle.cantidad * detalle.precio
        total += subtotal
        print(f"{p.codigo}  {p.denominacion}  {p.rubro}  {p.marca}  {detalle.cantidad}  {subtotal}")

    print(f"\nTOTAL: {total}")

    # Preguntar si desea generar archivo
    generar = input("¿Desea generar el archivo de esta orden? (S para generar): ").lower()
    if generar == "s":
        nombre_archivo = f"ordenCompra_nro_{orden.numero}.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(f"Orden de Compra N° {orden.numero}\n")
            f.write(f"Fecha: {orden.fecha}\n")
            f.write("------------ Productos Comprados ------------------------\n")
            f.write("Código  Denominación  Rubro   Marca   Cantidad SubTotal\n")
            for detalle in orden.detalles:
                p = detalle.producto
                subtotal = detalle.cantidad * detalle.precio
                f.write(f"{p.codigo}  {p.denominacion}  {p.rubro}  {p.marca}  {detalle.cantidad}  {subtotal}\n")
            f.write(f"\nTOTAL: {total}\n")
        print(f"Archivo '{nombre_archivo}' generado correctamente.")

    

#_________________________________________________________________________MAIN



"""1. Al ejecutar el programa lo primero que deberá realizar es leer el archivo de texto llamado 
productos_compra.txt, donde cada línea tiene el siguiente formato: 
Código;Denominación;Rubro;Marca;Precio Compra 
 
 
Ejemplo: 
1004;CARAMELOS SIN AZUCAR MENTA - ICY;SIN TACC;ICY;2460 
1005;HIERBAS GRANEL BETONICA;HIERBAS MEDICINALES;GRANEL;45714 
1006;EMPANADAS CARNE X 3 - PANYUCA;SIN TACC;PANYUCA;8821 
1007;AVENA INSTANTANEA X 350GR -DICOMERE;SIN TACC;DICOMERE;4362 
.......... 
Al leer el archivo deberá Generar un diccionario “ProductosDataBase” donde la clave es el código 
del producto y el valor será el objeto Producto correspondiente. """
#Código (numero), denominación (str), rubro(str), marca(str), precioCompra(numero)"""
def main():
    OrdenesDeCompra={}
    ProductosDataBase = {}
    listaordencompras=[]
    with open("productos_compra.txt", "r") as f:
        for linea in f:
            Codigo,Denominacion,Rubro,Marca,Precio_Compra  = linea.strip().split(";")
            elemento=producto(Codigo,Denominacion,Rubro,Marca,int(Precio_Compra))
            ProductosDataBase[Codigo]=elemento
    menu(ProductosDataBase,OrdenesDeCompra)

if __name__ == "__main__":
    main()