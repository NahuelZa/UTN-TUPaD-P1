alumnos={}

for i in range (1,2):
    nombre_alumno=input(f"Ingrese nombre alumno {i}: ")
    notas=[]
    for j in range (1,4):
        nota=float(input(f"Ingrese la nota {i} de {nombre_alumno}: "))
        notas.append(nota)
    alumnos[nombre_alumno]=tuple(notas)
print(alumnos)



for alumno,notas in alumnos.items():
    promedio=sum(notas)/len(notas)
    print(f"El promedio de {alumno} es {promedio} ")


# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.