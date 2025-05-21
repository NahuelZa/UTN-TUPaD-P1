#Funciones

def factorial (num):
    return 1 if num==0 else num*factorial(num-1)


#Programa Principal
num=int(input("ingrese numero: "))
for i in range (1,num+1):
    print(f"el factorial de {i} es {factorial(i)}")
# Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario