numero=int(input ("ingrese numero entero :"))

digitos=0

if numero >0:
    while numero >0:
        numero=round(numero/10)
        digitos+=1
    print("cantidad de digitos son", digitos )
elif numero ==0:
    print("cantidad de digitos son 1" )
else:
    print("ingrese numero mayor a 0")
