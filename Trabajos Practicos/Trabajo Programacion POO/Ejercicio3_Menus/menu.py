from platos import Plato
from ingredientes import Ingrediente

class MenuRestaurant: 
    def main():
        platos_menu = []

        print("CARGA DE PLATOS DEL MENÚ")

        while True:
            while True:
                nombre_plato = input("ingrese el nombre del plato: ")
                if nombre_plato.strip() == "" or nombre_plato.isdigit():
                    print("error: el nombre debe ser texto.")
                else:
                    break
            while True:
                precio_str = input("ingrese el precio del plato: ")
                try:
                    precio = float(precio_str)
                    break
                except ValueError:
                    print("error: el precio debe ser un número.")

            es_bebida = input("Es bebida? (s/n): ").lower() == "s"

            ingredientes = []

            if not es_bebida:
                while True:
                    cantidad_str = input("ingrese la cantidad de ingredientes: ")
                    if cantidad_str.isdigit():
                        cantidad = int(cantidad_str)
                        break
                    else:
                        print("error: debe ingresar un número entero.")

                for i in range(cantidad):
                    print(f"\ningrediente {i+1}:")
                    while True:
                        nombre_ing = input("nombre: ")
                        if nombre_ing.strip() == "" or nombre_ing.isdigit():
                            print("error: el nombre debe ser texto, no un número.")
                        else:
                            break

                    while True:
                        cantidad_ing_str = input("cantidad: ")
                        try:
                            cantidad_ing = float(cantidad_ing_str)
                            break
                        except ValueError:
                            print("error: la cantidad debe ser un número.")
                    while True:
                        unidad = input("unidad de medida: ")
                        if unidad.strip() == "" or unidad.isdigit():
                            print("error: la unidad debe ser texto, no un número.")
                        else:
                            break

                    nuevo_ing = Ingrediente(nombre_ing, cantidad_ing, unidad)
                    ingredientes.append(nuevo_ing)

            plato = Plato(nombre_plato, precio, es_bebida, ingredientes)
            platos_menu.append(plato)

            continuar = input("\ndesea agregar otro plato? (s/n): ").lower()
            if continuar != "s":
                break

        print("\n----------- MENÚ ----------------")
        for plato in platos_menu:
            plato.mostrar_info()

# Esto hace que se ejecute solo si abrís este archivo directamente:
if __name__ == "__main__":
    MenuRestaurant.main()
