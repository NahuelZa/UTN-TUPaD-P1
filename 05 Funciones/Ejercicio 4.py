#Funciones
import math

def calcular_area_circulo(radio):
    area=math.pi*radio**2
    print(f"El area del circulo es {area}")

def calcular_perimetro_circulo(radio):
    perimetro=radio*2*math.pi
    print(f"El perimetro del circulo es {perimetro}")
    

#Programa Principal
radio=float(input("ingrese radio: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)