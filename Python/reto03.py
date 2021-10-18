"""Elabore un programa en Python que lea un área en hectáreas y
 la convierta en metros cuadrados y muestre el resultado con un mensaje bien explicativo."""


while True:
    try:
        area= float (input("ingrese el área en hectáreas: "))
        break

    except:
        print("Error al ingresar el área")




def calcularArea (hectareas):
    areaMtsCuadrado = hectareas * 10000
    return areaMtsCuadrado

print("El área en metros cuadrado de", area, "hectareas es: ", calcularArea(area), "metros cuadrados.")

