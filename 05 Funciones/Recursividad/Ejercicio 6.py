#Funciones
def suma_digitos(n):
    if n==0:
        return 0
    else:
        digito=n%10
        return suma_digitos(n//10)+digito



#Programa Principal

print(suma_digitos(25))



# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.