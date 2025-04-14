#Funciones
def operaciones_basicas(a,b):
    print(f"{a} x {b} es igual a {a*b}")
    print(f"{a} / {b} es igual a {a/b}")
    print(f"{a} - {b} es igual a {a-b}")
    print(f"{a} + {b} es igual a {a+b}")


#Programa Principal
a=int(input("ingrese valor de a: "))
b=int(input("ingrese valor de b: "))
operaciones_basicas(a, b)