frase=input("Ingrese frase: ")
vocales="aeiou"
ultima=frase[len(frase)-1:len(frase)]

if ultima in vocales:
    print(frase + " !")
else:
    print(frase)

