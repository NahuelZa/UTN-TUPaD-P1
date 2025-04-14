#Funciones

def informacion_personal(nombre):
    nombre=input("Ingrese nombre: ")
    apellido=input("Ingrese apelldio: ")
    edad=int(input("Ingrese edad: "))
    residencia=input("Ingrese residencia: ")
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Programa Principal
informacion_personal()


