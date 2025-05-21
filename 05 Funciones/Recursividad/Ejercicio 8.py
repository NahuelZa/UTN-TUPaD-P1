#Funciones
def contar_digito(numero, digito):
    if numero==0:
        return 0
    else:
        num=numero%10
        if digito==num:
            return contar_digito(numero//10,digito)+1
        else:
            return contar_digito(numero//10,digito)
    



#Programa Principal

print(contar_digito(545,5))


# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
