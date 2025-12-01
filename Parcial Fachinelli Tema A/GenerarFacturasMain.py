from Articulo import articulo
from DetalleFactura import dertallefaactura
from Factura import factura 
from datetime import date

"""a- Ver Facturas Cargadas 
b- Cargar 1 o más Facturas 
c- Generar Archivo Factura por numero 
d- Salir"""
def Menu(articulosDataBase,facturasArmadas,veces):
    print("1-ver orden archivo orden compra") 
    print("2- generar orden de compra") 
    print("3- generar archivo de orden de compra") 
    print("4-salir")
    while True:
        eleccion=(input("ingerese su eleccion aqui: "))
        if eleccion=="1":
            verFacturasCargadas(facturasArmadas)
        elif eleccion=="2":
            CrearFactura(articulosDataBase,facturasArmadas,veces)
            veces +=1
            print("factura creada con exito")
        elif eleccion=="3":
            generarArchivo(facturasArmadas)
        elif eleccion=="4":
            print("saliendoo")
        else:
            print("introduzca una opcion valida")
            continue




"""a- Ver Facturas Cargadas: 
- Si se selecciona esta opción se deberá mostrar una lista de las facturas cargadas hasta el 
momento mostrando solo fecha, numero de factura y total"""
def verFacturasCargadas():
    with open("FacturasCargadas.txt","r") as f:
        lineas = f.readlines()
        if not lineas:
            print("No hay ninguna factura")
        else:
            for linea in lineas:
                print(linea.strip())

"""b- Cargar 1 o más Facturas 
- Para esta opción del menú se deberá crear una Factura asignar sus atributos y cargar su 
detalle correspondiente. Para la carga del detalle se deberá solicitar el código del artículo 
a cargar y obtenerlo del diccionario articulosDataBase, en caso de que el código no exista, 
indicarlo por pantalla y solicitarlo nuevamente. Se deberán cargar tantos detalles como 
se deseen hasta que el usuario indique que no quiere continuar. Validar que el atributo 
cantidad sea mayor a cero. Validar que se ingrese al menos 1 DetalleFactura. 
- Finalizada la carga de la Factura guardarla en una variable listaFacturas[] y preguntarle al 
usuario si quiere cargar una nueva factura. 
- Si indica que SI deberá repetir el proceso para una nueva factura"""
def mostrar_productos(articulosdatabase):
    print("\n--- LISTA DE PRODUCTOS ---")
    print("Código | Denominación | Rubro | Marca | Precio")
    for codigo, articulo in articulosdatabase.items():
        print(f"{codigo} | {articulo.denominacion} | {articulo.rubro} | {articulo.marca} | {articulo.precioVenta}")


def CrearFactura(articulosDataBase,facturasArmadas,veces):
    mostrar_productos(articulosDataBase)
    fechaHoy = date.today()
    facturaM=factura(fechaHoy,veces,[])

    while True:
        while True:
            cod=input("ingrese el codigo del producto: ")
            if cod in articulosDataBase:
                break
            else:
                print("el codigo no existe, intente de nuevo:")
                continue
        while True:
            cant=int(input("ingrese la cantidad del producto :"))
            if cant>0:
                break
            else:                    
                print("ingrese un numero mayor a 0: ")
                continue
        detalle=dertallefaactura(cant,articulosDataBase[cod],articulosDataBase[cod].precioVenta)
        facturaM.agregarDetalle(detalle)
        eleccion=input("ingrese si desea agregar otro detalle s/cualquier letra: ")
        eleccion.lower
        if eleccion=="s":
            print("iniciando de nuevo...")
            continue
        else:
            print("volviendo al menu...")
            facturasArmadas[veces]=facturaM #vital importancia que se ejecute
            break








"""c- Generar Archivo Factura por numero 
- Solicitar al usuario que ingrese un numero de factura; buscar la factura por su número en 
la listaFacturas[], si el número de factura no existe emitir el mensaje “La Factura con 
número XXXX no existe”. 
- Si la factura existe mostrarla por pantalla con el siguiente formato"""


"""Factura N° XXXXX 
Fecha: XXXXX 
------------ Articulos Vendidos ------------------------ 
Codigo  Denominación  Rubro   Marca   Cantidad SubTotal 
XXXXXX XXXXXX  XXXXXX XXXXXX XXXXXX XXXXXX  
 
         TOTAL: XXXXXX 
- Finalmente después de mostrar la factura por pantalla preguntar al usuario. 
¿Desea Generar el archivo de la Factura? Ingrese S para generar u otro carácter sino lo 
desea. 
Si el usuario ingresa S genere un archivo txt llamado factura_nro_XXXXX.txt con un 
formato lo similar posible al mostrado por pantalla."""

def generarArchivo(facturasArmadas):
    while True:
        cod=input("ingrese el numero de la orden para ver sus detalles : ")
        if cod in facturasArmadas:
            factura=facturasArmadas[cod]
            print(f"\nOrden de Compra N° {factura.numero}")
            print(f"Fecha: {factura.dia}")
            print("------------ Productos Comprados ------------------------")
            print("Código  Denominación  Rubro   Marca   Cantidad SubTotal")
    
            total = 0
            for detalle in factura.listadetalles:
                p = detalle.articulo
                subtotal = detalle.cantidad * detalle.subtotal
                total += subtotal
                print(f"{p.codigo}  {p.denominacion}  {p.rubro}  {p.marca}  {detalle.cantidad}  {subtotal}")
        else:
            print("ingrese un codigo valido...")
            continue


#__________________Main
"""1. Al ejecutar el programa lo primero que deberá realizar es leer el archivo de texto llamado 
articulos_venta.txt, donde cada línea tiene el siguiente formato:"""
"""Al leer el archivo deberá Generar un diccionario “articulosDataBase” donde la clave es el código 
del alumno y el valor será el objeto Artículo correspondiente."""
"""Código;Denominación;Rubro;Marca;Precio Venta"""
def main():
    articulosDataBase={}
    facturasArmadas={}
    veces=1
    with open ("articulos_venta.txt","r") as f:
        for filas in f:
            Codigo,Denominacion,Rubro,Marca,Precio_venta  = filas.strip().split(";")
            producto=articulo(Codigo,Denominacion,Rubro,Marca,Precio_venta)
            articulosDataBase[Codigo]=producto

    Menu(articulosDataBase,facturasArmadas,veces)


if __name__ == "__main__":
    main()






