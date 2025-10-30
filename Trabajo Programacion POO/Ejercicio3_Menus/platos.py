
class Plato:
    def __init__(self, nombre, precio, es_bebida, ingredientes):
        self.nombre = nombre
        self.precio = precio
        self.es_bebida = es_bebida
        self.ingredientes = ingredientes

    def mostrar_info(self):
        print("nombre del plato:", self.nombre)
        print("precio: $", self.precio)
        if not self.es_bebida:
            print("ingredientes:")
            print(f"{'Nombre':<11} {'Cantidad':<10} {'Unidad de Medida'}")
            for ing in self.ingredientes:
                print(ing)
        print("----------------------------------")