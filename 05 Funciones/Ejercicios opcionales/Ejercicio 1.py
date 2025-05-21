def es_capicua(n):
    numero=n
    reves=0    
    while numero>0:
        ultimo=numero%10
        reves=reves*10+ultimo
        numero=numero//10
    return n==reves
   


def capicuas_en_rango(inicio,fin):
    for i in range (inicio,fin):
        if len(str(i))>=2:
            resultado=es_capicua(i)
            if resultado is not None:
                print(resultado)




print(capicuas_en_rango(0,123))



