import random

def lanzar_dado():
    return random.randint(1,6)

def jugar(n):
    lista=[]
    repetidos=[]
    conteo={}
    
    for i in range (n):
        resultado=lanzar_dado()
        if resultado not in lista:
            lista.append(resultado)
        else:
            repetidos.append(resultado)
            
    for i in lista:
        contador=1
        for j in repetidos:
            if i==j:
                contador+=1                
                conteo[i]+=contador
            else:
                conteo[i]=contador
    return conteo
        

conteo=jugar(15)
for i,veces in conteo.items():
    print(f"el numero {i} salio {veces} veces")




# Definí una función lanzar_dado() que simule el lanzamiento de un dado de 6 caras. Luego,
# escribí una función jugar(n) que simule n lanzamientos y devuelva cuántas veces salió
# cada número.
# Pista: usar random.randint.