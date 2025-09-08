#este ejercicio esta siendo realizado nuevamente 
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper() #pido el hemisferio
mes = int(input("¿En qué mes estás? (1-12): ")) #pido el mes
dia = int(input("¿Qué día del mes es? (1-31): ")) #pido el dia


fecha = mes * 100 + dia  #transformo los numeros dados en numeros que pueda usar

if hemisferio == 'N':
    if (fecha >= 1221 or fecha <= 320):
        estacion = "Invierno"
    elif 321 <= fecha <= 620:
        estacion = "Primavera"
    elif 621 <= fecha <= 920:
        estacion = "Verano"
    elif 921 <= fecha <= 1220:
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"
elif hemisferio == 'S':
    if (fecha >= 1221 or fecha <= 320):
        estacion = "Verano"
    elif 321 <= fecha <= 620:
        estacion = "Otoño"
    elif 621 <= fecha <= 920:
        estacion = "Invierno"
    elif 921 <= fecha <= 1220:
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida"
else:
    estacion = "Hemisferio inválido"
print("La estación es:", estacion)
