stock={"Harina":100,"Golosinas":45,"Microfonos":5,"Pianos":9}
print("EL stock de que producto quisiera ver?")
print(list(stock))
opcion=input()
for productos,valores in stock.items():
    if opcion==productos:
        encontrado=True
        print(f"El stock de {opcion} es {valores}")
        print(f"Quisiera agregar stock?y/n")
        agregar=input().lower()
        if agregar=="y":
            monto=int(input(f"Indique cantidad a agregar: "))
            stock[opcion]+=monto
            print(f"Nuevo stock de {opcion} es {stock[opcion]}")
        else:
            print("bye")
            break
    else:
        encontrado=False
       
if encontrado==False:
    agregar=input(f"No se encontro el producto {opcion} quisiera agregarlo? y/n").lower()
    if agregar=="y":
        monto=int(input(f"Indique cantidad a agregar"))
        stock[opcion]=monto
        print("Nueva lista actualizada")
        print(stock)

    else:
        print("bye")
        
    


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.