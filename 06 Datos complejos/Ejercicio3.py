precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}

precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300

precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700
precios_frutas["Melón"]=2800

lista_sin_precios=[i for i in precios_frutas.keys()]
print(lista_sin_precios)
# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios