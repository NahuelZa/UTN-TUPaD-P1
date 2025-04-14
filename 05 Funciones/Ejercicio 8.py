#Funciones
def calcular_imc(peso,altura):
    imc=peso/altura**2
    print(f"Su IMC es {imc}")


#Programa Principal
peso=float(input("ingrese peso en kg: "))
altura=float(input("ingrese altura en m: "))
calcular_imc(peso, altura)