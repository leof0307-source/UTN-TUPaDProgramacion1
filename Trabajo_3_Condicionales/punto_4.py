
edad = int(input("Por favor, ingresa tu edad: "))

if edad < 12:
    print("categoria: niño/a")
elif edad < 18:
    print("categoria: adolescente")
elif edad < 30:
    print("categoria: adulto/a joven")
else:
    print("categoria: adulto/a")
    
