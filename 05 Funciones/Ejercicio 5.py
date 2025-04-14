#Funciones
def segundos_a_horas(seg):
    horas=seg/3600
    print(f"{seg} segundos en horas son {horas} horas")


#Programa Principal
segundos=int(input("ingrese segundos: "))
segundos_a_horas(segundos)