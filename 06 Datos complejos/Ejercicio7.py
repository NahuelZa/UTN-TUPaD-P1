aprobados_parcial_1={"Juan","Miguel","Luis","Pedro"}
aprobados_parcial_2={"Juan","Laura","Luis","Raul"}



print(f" Lista de aprobado que aprobaron los 2 Parciales:{aprobados_parcial_1.intersection(aprobados_parcial_2)}")
print(f" Lista de aprobado que aprobaron solo 1 Parcial:{aprobados_parcial_1.symmetric_difference(aprobados_parcial_2)}")
print(f" Lista de aprobado que aprobaron al menos 1 Parcial:{aprobados_parcial_1.union(aprobados_parcial_2)}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).