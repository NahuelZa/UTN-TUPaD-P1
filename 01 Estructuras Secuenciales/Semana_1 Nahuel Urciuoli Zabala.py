#Nahuel Urciuoli Zabala
#Actividad 1
print("Hola Mundo!")

#Actividad 2
nombre=input("Ingrese nombre: ")
print(f"Hola {nombre}!")

#Actividad 3
nombre=input("Ingrese nombre: ")
apellido=input("Ingrese apellido: ")
edad=input("Ingrese edad: ")
residencia=input("Ingrese residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Actividad 4
import math
radio=float(input("Ingrese radio criculo: "))
print(f"el area es {math.pi*radio**2} y perimetro es {2*math.pi*radio} ")

#Actividad 5
segundos=int(input("Ingrese segundos: "))
print(f"Eso serian {segundos/3600} horas")

#Actividad 6
numero=int(input("Ingrese numero: "))
for i in range (11):
    print (f"{numero} x {i} es igual a  {numero*i}")


#Actividad 7
numero=int(input("Ingrese numero distinto a 0: "))
numero2=int(input("Ingrese numero istinto a 0: "))
print (f"{numero} x {numero2} = {numero * numero2}")
print (f"{numero} + {numero2} = {numero + numero2}")
print (f"{numero} - {numero2} = {numero - numero2}")
print (f"{numero} / {numero2} = {numero / numero2}")

#Actividad 8
altura=int(input("Ingrese altura en cm: "))
peso=int(input("Ingrese peso: "))
altura=altura/100
print (f"su indice de masa corporal es", round(peso/altura**2))

#Actividad 9
temp=int(input("Ingrese temperatura: "))
print (f"en Fahrenheit son {(9/5)*temp+32}")


#Actividad 10
numero1=int(input("Ingrese numero: "))
numero2=int(input("Ingrese numero: "))
numero3=int(input("Ingrese numero: "))
print(f"el promedio es {(numero1+numero2+numero3)/3}")
