#Funciones
def celsius_a_fahrenheit(grados):
    fahrenheit=(grados*1.8)+32
    print(f"{grados} °C en Fahrenheit son {fahrenheit}")
    


#Programa Principal
celsius=int(input("Ingrese grados Celsius: "))
celsius_a_fahrenheit(celsius)