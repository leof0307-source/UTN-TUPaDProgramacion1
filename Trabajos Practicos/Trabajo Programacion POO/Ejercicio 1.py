# clase que representa una celda con fila, columna y valor
class Celda:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor


# clase matriz que guarda las celdas creadas
class Matriz:
    def __init__(self):
        self.celdasMatriz = []  # lista vacia

    # revisa si ya existe una celda en esa posicion
    def existe_posicion(self, fila, columna):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return True
        return False

    # agrega una nueva celda si no existe
    def agregar_celda(self, fila, columna, valor):
        if self.existe_posicion(fila, columna):
            print("ya hay una celda en esa posicion")
        else:
            nueva_celda = Celda(fila, columna, valor)
            self.celdasMatriz.append(nueva_celda)
            print("celda agregada")

    # muestra todas las celdas guardadas
    def mostrar_celdas(self):
        if len(self.celdasMatriz) == 0:
            print("no hay celdas cargadas")
        else:
            print("celdas cargadas:")
            for celda in self.celdasMatriz:
                print("fila:", celda.fila, "columna:", celda.columna, "valor:", celda.valor)

    # busca un valor segun la fila y columna
    def buscar_valor(self, fila, columna):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return celda.valor
        return "la fila y columna indicada no ha sido asignada en ninguna celda"


#Parte principal
matriz = Matriz()
seguir_carga = "s"

# ciclo para cargar las celdas
while seguir_carga == "s" or seguir_carga == "S":
    valor_celda = input("ingrese el valor de la celda (o 'fin' para salir): ")

    # si el usuario escribe fin se corta
    if valor_celda == "fin" or valor_celda == "FIN":
        break

    # si no pone nada
    if valor_celda == "":
        print("el valor no puede estar vacio")
    else:
        # pedir fila (se repite hasta que escriba algo)
        texto_fila = ""
        while texto_fila == "":
            texto_fila = input("ingrese fila: ")
            if texto_fila == "":
                print("no puede estar vacio")

        # pedir columna (se repite hasta que escriba algo)
        texto_columna = ""
        while texto_columna == "":
            texto_columna = input("ingrese columna: ")
            if texto_columna == "":
                print("no puede estar vacio")

        # convierte los valores a numero
        fila_ingresada = int(texto_fila)
        columna_ingresada = int(texto_columna)

        # agrega la celda
        matriz.agregar_celda(fila_ingresada, columna_ingresada, valor_celda)

    seguir_carga = input("desea agregar otra celda? (s/n): ")

# muestra todas las celdas cargadas
matriz.mostrar_celdas()

# parte de busqueda
seguir_busqueda = "s"

while seguir_busqueda == "s" or seguir_busqueda == "S":
    print("buscar una celda especifica para visualizar su contenido")

    # pedir fila a buscar
    texto_fila_buscar = ""
    while texto_fila_buscar == "":
        texto_fila_buscar = input("fila: ")
        if texto_fila_buscar == "":
            print("no puede estar vacio")

    # pedir columna a buscar
    texto_columna_buscar = ""
    while texto_columna_buscar == "":
        texto_columna_buscar = input("columna: ")
        if texto_columna_buscar == "":
            print("no puede estar vacio")

    # convierte los valores a numero
    fila_buscar = int(texto_fila_buscar)
    columna_buscar = int(texto_columna_buscar)

    print("resultado:", matriz.buscar_valor(fila_buscar, columna_buscar))
    seguir_busqueda = input("desea buscar otra celda? (s/n): ")

print("programa terminado")

