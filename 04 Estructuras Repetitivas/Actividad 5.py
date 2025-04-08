import random
numero_pc=random.randint(0,9)
numero_jugador=int(input("ingrese numero entre 0 y 9 "))
intentos=1
while numero_pc!=numero_jugador:
    numero_jugador=int(input("fayo ingrese otro numero: "))
    intentos+=1

print(f"adivino despues de {intentos} intentos")