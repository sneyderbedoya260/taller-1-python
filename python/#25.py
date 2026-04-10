numero_ventas = int(input("Ingrese el número de ventas realizadas en el día: "))

total = 0

for i in range(numero_ventas):
    valor_venta = float(input("Ingrese el valor de la venta: "))
    total += valor_venta

promedio = total / numero_ventas if numero_ventas > 0 else 0

print("Total vendido: $", total)
print("Promedio por venta: $", promedio)
