magnitud=int(input("Ingrese magnitud: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud >=3 and magnitud <4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("AModerado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte")
elif magnitud >= 7:
    print("Extremo")