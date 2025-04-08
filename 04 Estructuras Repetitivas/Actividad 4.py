fin="0"
suma=0

numero=int(input("ingrese numero entero (presione "  +fin+ " para terminar :)"))
while numero !=0:
    suma+=numero
    numero=int(input("ingrese numero entero (presione "  +fin+ " para terminar :)"))
print(suma)