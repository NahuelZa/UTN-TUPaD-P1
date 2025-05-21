
def filtrar_por_longitud(palabras,longitud_min):
    lista=[]
    for i in palabras:
        if len(i)>=longitud_min:            
            lista.append(i)
        else:
            pass
    return lista




palabras=['sol','luna','universo',]
longitud=4
print(filtrar_por_longitud(palabras,longitud))






# Escribí una función filtrar_por_longitud(palabras, longitud_min) que reciba una lista de
# palabras y un número, y devuelva una nueva lista con solo las palabras que tienen una
# longitud mayor o igual a la indicada.
# Ejemplo:
# filtrar_por_longitud(['sol', 'luna', 'universo'], 5) → ['luna', 'universo']



