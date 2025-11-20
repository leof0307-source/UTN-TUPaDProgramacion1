#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.
alumnos={}

cantidad_alumnos=int(input("Ingrese la cantidad de alumnos:"))
for i in range (cantidad_alumnos):
    nombre=input("Ingrese el nombre del alumno:")
    notas=[]
    for j in range (3):
        nota=float(input(f"Ingrese la nota {j+1} de {nombre}:"))
        notas.append(nota)
    alumnos[nombre]=tuple(notas)
print(alumnos)
for alumno, notas in alumnos.items():
    promedio=sum(notas)/len(notas)
    print(f"El promedio de {alumno} es {promedio}")