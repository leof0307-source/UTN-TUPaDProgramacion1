#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

set1={1,3,4,6,7,8,9,11}
set2={1,2,4,5,6,7,8,10}
if set1 & set2:                       #aqui investigue sobre la insterseccion de sets
    print(f"Los estudiantes que aprobaron ambos parciales son: {set1 & set2}")
     
solo_uno = set1 ^ set2
print(f"Estudiantes que aprobaron solo uno de los parciales: {solo_uno}")

al_menos_uno = set1 | set2
print(f"Estudiantes que aprobaron al menos un parcial: {al_menos_uno}")
