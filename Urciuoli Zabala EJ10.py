import datetime

Hemisferio= input("Ingrese N o S ")

año = datetime.datetime.now().year
mes = int(input("Eliga mes (1-12) "))
dia = int(input("Eliga dia "))

Fecha= datetime.date(año, mes, dia)

# inicio / Fin primavera norte y sur
inicio_primavera_norte=datetime.date(año,3,21)
fin_primavera_norte=datetime.date(año,6,20)


inicio_Primavera_sur=datetime.date(año,9,21)
fin_Primavera_sur=datetime.date(año,12,20)
#inicio / Fin verano norte y sur
inicio_verano_sur=datetime.date(año,12,21)
fin_verano_sur=datetime.date(año+1,3,20)

inicio_Verano_norte=datetime.date(año,6,21)
fin_Verano_norte=datetime.date(año,9,20)

#Inicio / Fin Otoño norte y sur
inicio_Otoño_sur=datetime.date(año,3,21)
fin_Otoño_sur=datetime.date(año,6,20)

inicio_Otoño_norte=datetime.date(año,9,21)
fin_Otoño_norte=datetime.date(año,12,20)

#Inicio / Fin Iniverno norte y sur
inicio_invierno_norte=datetime.date(año,12,21)
fin_invierno_norte=datetime.date(año+1,3,20)

inicio_Invierno_sur=datetime.date(año,6,21)
fin_Invierno_sur=datetime.date(año,9,20)


if Hemisferio=="N" or Hemisferio== "n" :
    if inicio_invierno_norte<=Fecha<=fin_invierno_norte:
        print("Invierno")
    elif inicio_primavera_norte<=Fecha<=fin_primavera_norte:
        print("Primavera")
    elif inicio_Verano_norte<=Fecha<=fin_Verano_norte:
        print("Verano")
    elif inicio_Otoño_norte<=Fecha<=fin_Otoño_norte:
        print("Otoño")
    else:
        print("no valido")

if Hemisferio == "S" or Hemisferio=="s":
    if inicio_Invierno_sur<=Fecha<=fin_Invierno_sur:
        print("Invierno")
    elif inicio_Primavera_sur<=Fecha<=fin_Primavera_sur:
        print("Primavera")
    elif inicio_verano_sur<=Fecha<=fin_verano_sur:
        print("Verano")
    elif inicio_Otoño_sur<=Fecha<=fin_Otoño_sur:
        print("Otoño") 
    else:
        print("no valido")