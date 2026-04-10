edad = int(input("Ingrese la edad: "))

if edad < 18:
    print("Es menor de edad")
elif edad >= 18 and edad < 60:
    print("Es adulto")
else:
    print("Es adulto mayor")
