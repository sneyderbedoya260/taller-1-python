capital = float(input("Ingrese el capital inicial: "))
tasa_interes = float(input("Ingrese la tasa de interés (por ejemplo 0.05 para 5%): "))
periodos = int(input("Ingrese el número de períodos: "))

monto_final = capital * (1 + tasa_interes) ** periodos

print("Monto final:", monto_final)
