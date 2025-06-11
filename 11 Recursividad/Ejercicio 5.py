#Funciones
def validacion(palabra):
    def es_palindromo(palabra): 
        if len(palabra)==0:
            return ""
        else:
            return palabra[-1]+es_palindromo(palabra[0:len(palabra)-1])
    
    if es_palindromo(palabra)==palabra:
        return True
    else:
        return False
        




#Programa Principal

print(validacion("sa"))



# Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es