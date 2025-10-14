
def validarnumero(numero):
    try:
        int(numero)
        return True
    except ValueError:
        print("el legajo no es numérico ingrese datos correctos")
        return False

def agregardiccionario(alumnos):
    with open("alumnosynotas.txt","r") as archivo:
        for linea in archivo:
            partes=linea.strip().split(",")
            nombre=partes[0]
            apellido=partes[1]
            legajo=partes[2]
            nota=partes[3]
            valor = (f"{nombre},{apellido},{nota}")
            clave=legajo
            alumnos[clave]=valor
    return alumnos

def agregaralumno(alumnos):
    bandera = True

    while bandera:
        nombre = input("Ingrese el nombre: ")
        if not nombre.isalpha():
            print("el nombre solo debe contener letras.")
            continue  
        break 

    while True:
        apellido = input("Ingrese el apellido: ")
        if not apellido.isalpha():
            print("El apellido solo debe contener letras.")
            continue
        break

    while True:
        legajo = input("Ingrese el legajo: ")
        if not validarnumero(legajo):
            print("el legajo debe ser numérico.")
            continue
        if legajo in alumnos:
            print("ese legajo ya existe.")
            continue
        break

    while True:
        nota = input("engrese la nota con punto si es que se requiere: ")
        if not validarnumero(nota):
            print("la nota debe ser numérica.")
            continue
        break

    aux=(f"{nombre},{apellido},{legajo},{nota}\n")
    existe=validar_existe_alumno(aux)
    if existe:
        with open("alumnosynotas.txt", "a") as archivo:
            archivo.write(f"{nombre},{apellido},{legajo},{nota}\n")
            agregardiccionario(alumnos)
            return alumnos
    else:
        print("el alumno no se agrego")

def validar_existe_alumno(aux):
    with open("alumnosynotas.txt", "r") as archivo:
        for linea in archivo:
            if linea.strip() == aux.strip():
                print("este alumno ya existe")
                return False
    return True

def leerarchivo():
    with open("alumnosynotas.txt", "r") as archivo:
        contenido = archivo.read().strip()

    if not contenido:
        print("el archivo está vacío.")

def dar_aprovados():
    with open("alumnosynotas.txt","r") as archivo:
        for linea in archivo:
            partes=linea.strip().split(",")
            nombre=partes[0]
            apellido=partes[1]
            legajo=partes[2]
            nota=partes[3]
            if float(nota) >= 6:
                with open("aprobados.txt","a") as archivo: #aca se puede dejar antes de todo el bloque para que no se abra y se cierre el archivo
                    archivo.write(f"{nombre},{apellido},{legajo},{nota}\n")
            else:
                pass




partes=[]
alumnos={}


####################
#codigo principal pe
#####################
partes = []
alumnos = {}

try:
    with open("alumnosynotas.txt", "r") as f:
        print("El archivo existe.")
except FileNotFoundError:
    print("El archivo NO existe. Creando uno nuevo...")
    open("alumnosynotas.txt", "w").close()



bandera = True
while bandera:
    print("\n--- MENÚ ---")
    print("1. agregar alumno")
    print("2. mostrar alumnos")
    print("3. generar lista de aprobados")
    print("4. salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        agregaralumno(alumnos)

    elif opcion == "2":
        leerarchivo()

    elif opcion == "3":
        dar_aprovados()

    elif opcion == "4":
        print("saliendoooooo")
        bandera = False

    else:
        print("ppcion no válida. intente de nuevo.")
print(alumnos)
