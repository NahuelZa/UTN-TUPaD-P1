numero1=int(input("ingrese un numero: "))
numero2=int(input("ingrese otro numero: "))

suma=0
if numero1<numero2:
    for i in range (numero1+1,numero2):
        suma+=i
    print (suma)
elif numero1>numero2:
    for i in range (numero2+1,numero1):
        suma+=i
    print (suma)