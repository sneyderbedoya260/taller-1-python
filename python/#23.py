peso = float(input("Ingrese el peso del paquete en kg: "))

if peso <= 5:
    costo = 10000
else:
    costo = 20000

print("El costo del envío es: $", costo)
