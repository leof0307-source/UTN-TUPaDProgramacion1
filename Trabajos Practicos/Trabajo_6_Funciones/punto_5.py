#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mos
#rar el resultado usando esta función.
def segundos_a_horas(segundos):
    return segundos / 3600
segundos=float(input("ingrese la cantidad de segundos: "))
print (f"la cantidad de segundos en horas es: {segundos_a_horas(segundos)}")
