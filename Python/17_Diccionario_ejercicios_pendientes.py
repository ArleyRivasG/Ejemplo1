""" #2
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio
de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello."""

dic_frutas = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}


calcular = "si"
while calcular == "si":
    fruta = input("ingrese la fruta: ")
    fruta=fruta.capitalize() #El método capitalize() devuelve un string en el que solo la primera letra estará escrita en mayúsculas:
    print(fruta)

    if (fruta in dic_frutas):
        cantidad = int(input("ingrese los kilos  de la fruta: "))
        precio = dic_frutas[fruta]
        print(precio)
        valor = precio * cantidad
        print("el valor de ", cantidad, "kilos de", fruta, "es $", valor, )
    else:
        print("Fruta no encontrada")

    calcular = input("Desea calcular otro precio? (si \ no): ")


"""4. Escribe un programa python que pida un número por teclado y que cree 
un diccionario cuyas claves sean desde el número 1 hasta el 
número indicado, y los valores sean los cuadrados de las claves. """

import math as m

def crear_Dicc(numDatos = int(input("ingrese el tamaño del Diccionario: "))):
    dicc_datos={}

    for i in range(numDatos):
        dicc_datos[i+1]= m.pow(i+1,2) # i+1 ya que queremos arrancar claves en 1 y no en 0

    print(dicc_datos)
    return dicc_datos


crear_Dicc() #se puede asignar lo que retorna (Diccionario) a una variable para trabajar con ella





