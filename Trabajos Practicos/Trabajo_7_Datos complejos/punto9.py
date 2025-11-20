#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.
# Creamos la agenda con algunos eventos
agenda = {
    ("Lunes", "9:00"): "Reunión de equipo",
    ("Martes", "14:00"): "Clase de inglés",
    ("Miércoles", "10:30"): "Ir al gimnasio",
    ("Viernes", "18:00"): "Cine con amigos"
}

# Pedimos al usuario un día y una hora para consultar
dia = input("Ingresá el día: ")
hora = input("Ingresá la hora (por ejemplo 9:00): ")

# Creamos una tupla con los datos
clave = (dia, hora)

# Verificamos si está en la agenda
if clave in agenda:
    print("Tenés:", agenda[clave])
else:
    print("No tenés nada agendado en ese horario.")
