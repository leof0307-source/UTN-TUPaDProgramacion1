#Importación de clases ---------------------
from claseComputadora import Computadora
from claseComponentes_cpu import ComponenteCPU

#Funciones de verificación -----------------

def input_obligatorio(mensaje):
    #Verifica que un texto no esté vacio

    while True: 
        texto = input(mensaje).strip()

        if texto != "":
            return texto
        else:
            print("El campo no puede estar vacío. Intente nuevamente...")

def numeroEntero(mensaje):
    #Verifica si el número que se ingresa es entero positivo
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            else:
                print("Debe ingresar un número mayor que cero")
        except ValueError:
            print("Debe ingresar un número entero válido")

def numeroDecimal(mensaje):
    #Verifica que el número sea decimal positivo
    while True:
        try:
            numero = float(input(mensaje))
            if numero >= 0:
                return numero
            else:
                print("El precio no puede ser negativo.")
        except ValueError:
            print("Debe ingresar un número válido")



#Código principal ---------------------------
def main():

    nuevoIngreso = True    
    
    while nuevoIngreso:

        marca = input_obligatorio("Ingrese la marca de la computadora: ").title()
        modelo = input_obligatorio("Ingrese el modelo de la computadora: ")
        
        pc = Computadora(marca, modelo)

        componentesCantidad = numeroEntero("Ingrese el número de componentes del CPU: ")

        print("\n----INGRESAR DATOS DE LOS COMPONENTES----")

        for i in range(1, componentesCantidad + 1):
            print(f"\nComponente {i}:")
            nombreComponente = input_obligatorio("Nombre: ")
            marcaComponente = input_obligatorio("Marca: ")
            cantidadComponente = numeroEntero("Cantidad: ")
            precioComponente = numeroDecimal("Precio: ")

            componente = ComponenteCPU(nombreComponente, marcaComponente, cantidadComponente, precioComponente)

            pc.agregar_componente(componente)

        print("\n------COMPUTADORA------")
        print(f"""
        Marca: {marca}
        Modelo: {modelo}
        \n""")
        
        print("Componentes...\n")
        for componentes in pc.componentesCPU:
            subtotal = componentes.cantidad * componentes.precio

            print(f"Componente: {componentes.componente} | Marca: {componentes.marca} | Cantidad: {componentes.cantidad} | Precio x Unidad: ${componentes.precio} | Subtotal: ${subtotal}")

        costo = pc.costo_total()
        precio_venta = pc.precio_venta_sugerido()

        print(f"Costo total: ${costo}")
        print(f"Precio sugerido de venta: ${precio_venta}")


        opcionValida = False 

        while not opcionValida:
            opcion = input("¿Desea cotizar una nueva computadora? (SI/NO): ").lower().strip()

            if opcion == "si":
                opcionValida = True
            elif opcion == "no":
                nuevoIngreso = False 
                opcionValida = True
            else:
                print("La opción ingresada no es válida, intente nuevamente...")


if __name__ == "__main__":
    main()