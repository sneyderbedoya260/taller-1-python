pesos = float(input("Ingrese el valor en pesos colombianos: "))
tasa_cambio = float(input("Ingrese la tasa de cambio (pesos por dólar): "))

dolares = pesos / tasa_cambio

print("Equivale a:", dolares, "dólares")
