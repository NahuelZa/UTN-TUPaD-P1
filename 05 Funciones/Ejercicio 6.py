#Funciones
def tabla_multiplicar(num):
    for i in range (1,11):
        print(f"{num} x {i} es igual a {num*i}")


#Programa Principal
numero=int(input("Ingrese numero a multiplicar: "))
tabla_multiplicar(numero)