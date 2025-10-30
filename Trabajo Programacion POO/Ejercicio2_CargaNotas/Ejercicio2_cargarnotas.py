from alumno import Alumno
from nota import Nota

def main():
    alumnos = []

    while True:
        print("\n--- INGRESE DATOS DEL ALUMNO ---")

        # --- Validar nombre ---
        while True:
            nombre = input("Ingrese nombre completo: ").upper()
            if nombre.strip() == "" or nombre.isdigit():
                print("Error: el nombre no puede estar vacío ni ser un número.")
                continue
            if not all(c.isalpha() or c.isspace() for c in nombre):
                print("El nombre solo puede contener letras y espacios.")
                continue
            if any(a.nombreCompleto == nombre for a in alumnos):
                print("El nombre ya existe, intente otro.")
                continue
            break

        # --- Validar legajo ---
        while True:
            legajo = input("Ingrese legajo (5 dígitos): ")
            if not legajo.isdigit():
                print("Error: el legajo debe contener solo números.")
                continue
            if len(legajo) != 5:
                print("El legajo debe tener exactamente 5 dígitos numéricos.")
                continue
            if any(a.legajo == int(legajo) for a in alumnos):
                print("El legajo ya existe, intente otro.")
                continue
            break

        alumno = Alumno(nombre, int(legajo))

        while True:
            print("\n--- INGRESE NOTA DEL ALUMNO ---")

            # --- Validar nombre de cátedra ---
            while True:
                catedra = input("Ingrese nombre de cátedra: ")
                if catedra.strip() == "" or catedra.isdigit():
                    print("Error: la cátedra no puede estar vacía ni ser un número.")
                    continue
                if not all(c.isalpha() or c.isspace() for c in catedra):
                    print("La cátedra solo puede contener letras y espacios.")
                    continue
                break

            # --- Validar nota numérica ---
            while True:
                nota_input = input("Ingrese nota (1-10): ")
                try:
                    notaExamen = float(nota_input)
                    if notaExamen < 1 or notaExamen > 10:
                        print("La nota debe estar entre 1 y 10.")
                        continue
                    break
                except ValueError:
                    print("Ingrese un número válido.")
                    continue

            nota = Nota(catedra, notaExamen)
            alumno.agregar_nota(nota)

            # --- Validar salida de carga de notas ---
            while True:
                salirNotas = input("¿Desea salir de la carga de notas? (s/n): ").lower()
                if salirNotas not in ["s", "n"]:
                    print("Debe ingresar 's' o 'n'.")
                    continue
                break

            if salirNotas == "s":
                if len(alumno.notas) >= 1:
                    break
                else:
                    print("Debe ingresar al menos una nota antes de salir.")

        alumnos.append(alumno)

        # --- Validar salida de carga de alumnos ---
        while True:
            salirAlumno = input("\n¿Desea salir de carga de alumnos? (s/n): ").lower()
            if salirAlumno not in ["s", "n"]:
                print("Debe ingresar 's' o 'n'.")
                continue
            break

        if salirAlumno == "s":
            break

    print("\n--- INFORMACIÓN DE ALUMNOS ---")
    for a in alumnos:
        print("\nAlumno:", a.nombreCompleto, "| Legajo:", a.legajo)
        for n in a.notas:
            print("Cátedra:", n.catedra, "| Nota:", n.notaExamen)
        print("Promedio:", round(a.calcular_promedio(), 2))
        print("-----------------------------")


if __name__ == "__main__":
    main()
