

pares=0
impares=0
negativos=0
positivos=0

for i in range (100):
    numero=int(input("ingrese numero entero "))
    if numero%2==0:
        pares+=1
    else:
        impares+=1

    if numero<0:
        negativos+=1
    else:
        positivos+=1

print(f"cantidad de numeros pares son {pares}")
print(f"cantidad de numeros impares son {impares}")
print(f"cantidad de numeros negativos son {negativos}")
print(f"cantidad de numeros positivos son {positivos}")

