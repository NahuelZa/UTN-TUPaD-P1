agenda={('Lunes', '10:00'): 'Paparazzi',
        ('Martes', '11:00'): 'Reunion'}

horario=[]
dia=input("Que dia tiene la actividad? ")
hora=input("Que hora tiene la actividad ")
horario.append(dia)
horario.append(hora)
actividad=input("Que actividad tiene? ")
agenda[tuple(horario)]=actividad

print(agenda)

print("Que dia y hora quiere consultar? ")
consulta_dia=input("Ingrese dia: ")
consulta_hora=input("Ingrese hora: ")
encontrado=True
for i in agenda.keys():
    dia,hora=i   
    if consulta_dia==dia and consulta_hora==hora:
        print(agenda[i],"es la actividad que tiene")
        break
    else:        
        encontrado=False
        
if encontrado==False:
    print(f"no tiene nada el dia {consulta_dia} a las {consulta_hora} ")
        
 
# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
