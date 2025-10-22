def contar_bloques(bloques):
    if bloques==1:
        return 1
    else:
        return bloques+contar_bloques(bloques-1)

bloques_iniciales=int(input("ingrese la cantidad de bloques iniciales: "))
print(f"para construir la pramide con {bloques_iniciales} iniciales, se necesitan {contar_bloques(bloques_iniciales)}")