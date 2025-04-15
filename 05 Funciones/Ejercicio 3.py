#Funciones

def informacion_personal(nombre,apellido,edad,residencia): 
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Programa Principal
nombre=input("Ingrese nombre: ")
apellido=input("Ingrese apelldio: ")
edad=int(input("Ingrese edad: "))
residencia=input("Ingrese residencia: ")

informacion_personal(nombre,apellido,edad,residencia)


