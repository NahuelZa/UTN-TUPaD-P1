#Funciones
def contar_bloques(base):
    if base==1:
        return 1
    else:
        return contar_bloques(base-1)+base




#Programa Principal

print(contar_bloques(4))




# Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
