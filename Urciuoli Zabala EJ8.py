nombre=input("ingrese nombre: ")
print("Ingrece opcion \n 1 Para Mayusculas \n 2 para minusculas \n 3 Si solo quiere la primera letra del nombre en mayusculas  ")
choice=int(input("Ingrese numero : "))
if choice == 1:
    print (nombre.upper())
elif choice == 2 :
    print(nombre.lower())
elif choice == 3:
    print (nombre.title())