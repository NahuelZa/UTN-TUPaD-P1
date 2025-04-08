import math
numero=int(input("ingrese un numero: "))
invertido=0

while numero>0:
    ultimo_digito=numero%10
    invertido=(invertido*10)+ultimo_digito
    numero=math.trunc(numero/10)
print(invertido)

