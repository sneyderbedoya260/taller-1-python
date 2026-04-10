import math

radio = float (input("ingrese el radio del circulo"))
#area =pi * radio ^ 2
area = math.pi * math.pow(radio, 2)
#area =pi * radio * radio 
perimetro = 2 * math.pi * radio
print("Area: ", round (area, 2))
print("perimetro : ", round (perimetro, 2))