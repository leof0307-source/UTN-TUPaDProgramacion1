#C�digo;Denominaci�n;Rubro;Marca;Precio Compra

from producto import Producto
from detalleordencompra import DetalleOrdenCompra
from datetime import datetime  


PRODUCTS_FILE = "productos_compra.txt"
ORDERS_FILE = "listaCompra.txt"

def cargar_productos(ruta=PRODUCTS_FILE):
    productos = {}
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                partes = [p.strip() for p in linea.split(";")]
                if len(partes) < 5:
                    continue
                codigo = partes[0]
                denominacion = partes[1]
                rubro = partes[2]
                marca = partes[3]
                precio_raw = partes[4]
                try:
                    precio = float(precio_raw.replace(",", "."))
                except Exception:
                    precio = 0.0
                productos[codigo] = {
                    "codigo": codigo,
                    "denominacion": denominacion,
                    "rubro": rubro,
                    "marca": marca,
                    "precio": precio
                }
    except FileNotFoundError:
        pass
    return productos

def proximo_numero_orden(ruta=ORDERS_FILE):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()
            return contenido.count("OrdenCompra:") + 1
    except FileNotFoundError:
        return 1

def guardar_orden_texto(fecha, numero, total, detalles, ruta=ORDERS_FILE):
    with open(ruta, "a", encoding="utf-8") as f:
        f.write(f"OrdenCompra: {numero} | Fecha: {fecha} | Total: {total:.2f}\n")
        for d in detalles:
            f.write(f"  - Codigo: {d.producto.codigo} | Cantidad: {d.cantidad} | Subtotal: {d.subtotal:.2f}\n")
        f.write("\n")

def crear_orden_interactiva(productos):
    fecha = datetime.today().strftime("%d/%m/%Y")
    numero = proximo_numero_orden()
    detalles = []
    total = 0.0
    while True:
        codigo = input("Ingrese el codigo del producto (o ENTER para terminar la orden): ").strip()
        if codigo == "":
            break
        if codigo not in productos:
            print("Codigo no encontrado. Intente de nuevo.")
            continue
        prod_info = productos[codigo]
        while True:
            qty_str = input(f"Ingrese la cantidad para '{prod_info['denominacion']}': ").strip()
            try:
                cantidad = float(qty_str)
                if cantidad <= 0:
                    raise ValueError
                break
            except Exception:
                print("Cantidad inválida. Ingrese un número mayor que 0.")
        precio = prod_info["precio"]
        subtotal = cantidad * precio
        prod_obj = Producto(prod_info["codigo"], prod_info["denominacion"], prod_info["rubro"], prod_info["marca"], precio)
        detalle = DetalleOrdenCompra(cantidad, prod_obj, subtotal)
        detalles.append(detalle)
        total += subtotal
        print(f"Agregado: {prod_info['denominacion']} x{cantidad} -> subtotal {subtotal:.2f}")
    if not detalles:
        print("Orden vacía. No se guardó.")
        return
    guardar_orden_texto(fecha, numero, total, detalles)
    print(f"Orden {numero} guardada. Total: {total:.2f}")

def main():
    productos = cargar_productos()
    while True:
        print("\n--- MENU ---")
        print("1 = Ver lista de compras")
        print("2 = Cargar 1 o mas ordenes de compra")
        print("3 = Generar Archivo Orden de Compra por numero (ver)")
        print("4 = Salir")
        eleccion = input("Elija una opcion: ").strip()
        if eleccion == "1":
            try:
                with open(PRODUCTS_FILE, "r", encoding="utf-8") as f:
                    print(f.read())
            except FileNotFoundError:
                print("No existe el archivo de lista de compras.")
        elif eleccion == "2":
            crear_orden_interactiva(productos)
        elif eleccion == "3":
            num = input("Ingrese el numero de orden a mostrar: ").strip()
            try:
                with open(ORDERS_FILE, "r", encoding="utf-8") as f:
                    contenido = f.read()
                    bloques = contenido.split("\n\n")
                    encontrado = False
                    for b in bloques:
                        if b.strip().startswith(f"OrdenCompra: {num} "):
                            print(b)
                            encontrado = True
                            break
                    if not encontrado:
                        print("Orden no encontrada.")
            except FileNotFoundError:
                print("No existe el archivo de lista de compras.")
        elif eleccion == "4":
            break
        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    main()
