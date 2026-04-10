capital = float(input("Ingrese el capital: "))
tasa_interes = float(input("Ingrese la tasa de interés (por ejemplo 0.05 para 5%): "))
tiempo_meses = float(input("Ingrese el tiempo en meses: "))

interes = capital * tasa_interes * tiempo_meses
total = capital + interes

print("Interés generado:", interes)
print("Total a pagar:", total)
