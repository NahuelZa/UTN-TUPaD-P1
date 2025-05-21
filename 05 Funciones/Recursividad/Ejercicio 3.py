#Funciones

def potencia(num,potencia):
    if potencia==0:
        return 0
    else:
        return num*num**(potencia-1)


print(potencia(5,5))
#Programa Principal

# Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1). Prueba esta función en un algoritmo general.