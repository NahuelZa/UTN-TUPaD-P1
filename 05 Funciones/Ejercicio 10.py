#Funciones
def calcular_promedio(primero,segundo,tercero):
    promedio=(primero+segundo+tercero)/3
    print(f"El promedio de los 3 numero es {promedio}")


#Programa Principal
a=float(input("Ingrese primer numero: "))
b=float(input("Ingrese segundo numero: "))
c=float(input("Ingrese tercer numero: "))
calcular_promedio(a, b, c)