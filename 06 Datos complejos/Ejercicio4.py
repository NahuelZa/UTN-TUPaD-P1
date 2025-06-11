contactos={}
for i in range (1,7):
    nombre=input(f"Escriba nombre de contacto numero {i}: ")
    numero=input(f"Escriba el numero de contacto numero {i}: ")
    contactos[nombre]=numero


for nombre, numero in contactos.items():
    print(f"{nombre}: {numero}")

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.