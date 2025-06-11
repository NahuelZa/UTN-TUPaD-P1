frase=input("Ingrese frase: ")


palabras_unicas=set()
cantidad_palabras={}
for i in frase.split():
    palabras_unicas.add(i)
    if i not in cantidad_palabras:
        cantidad_palabras[i]=1
    else:
        cantidad_palabras[i]+=1


print(palabras_unicas)
print(cantidad_palabras)

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra