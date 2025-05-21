#Funciones
def binario_a_texto(numero):
    if numero==0:
        return ""
    else:            
        return binario_a_texto(numero//2)+str(numero%2)
    


print(binario_a_texto(2))
        






#Programa Principal

