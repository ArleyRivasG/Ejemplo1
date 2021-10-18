import math

""" RESOLVER EL FACTORIAL DE UN NUMERO"""

"""numfact = int(input("please ingrese un numero entero para conocer su factorial: "))
if (numfact > 0):
    factorial = numfact
    condicion = numfact

    while (condicion > 1):
        condicion -= 1
        factorial = factorial * condicion
else:
    print("please ingrese un numero mayor a 0")
print(f"el factorial de {numfact} es: {factorial}")
"""

numfact=0
while (numfact==0 or numfact<0):
    numfact = int(input("please ingrese un numero entero positivo para conocer su factorial: "))

factorial = numfact
condicion = numfact

while (condicion > 1):
    condicion -= 1
    factorial = factorial * condicion

print(f"el factorial de {numfact} es: {factorial}")


"""Factorial con libreria"""


# pedimos el numero y rompemos el while solo cuando ingresen un numero y a su vez sea mayor que 0
while True:
    numeroFact = input("ingrese el numero entero a evaluar factorial: ")

    if numeroFact.isdigit():
        numeroFact = int(numeroFact)
        if (numeroFact != 0):
            break
        print("por favor ingrese solo numero entero positivo ")


print(f"El factorial de {numeroFact} es: {math.factorial(numeroFact)}")
#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

# pedimos el numero y rompemos el while solo cuando ingresen un numero y a su vez sea mayor que 0
while True:
    numEntrada = input("ingrese un numero entero: ")

    if numEntrada.isdigit():
        numEntrada = int(numEntrada)
        break
    print("por favor ingrese solo numero o 0 para finalizar")

sumaEntero = 0
while (numEntrada != 0):

    sumaEntero = sumaEntero + (numEntrada)
    while True:
        numEntrada = input("ingrese el numero entero: ")

        if numEntrada.isdigit():
            numEntrada = int(numEntrada)
            print(numEntrada)
            break

print("La suma de los numeros es:", sumaEntero)


#7. Crea un programa en el que el usuario introduzca números enteros hasta adivinar el número aleatorio entre 0 y 100 generado al azar por el ordenador.
# El programa debe avisar si el número introducido por el usuario es más grande o más pequeño que el número generado aleatoriamente.

import random

numOrdenador=int((random.randrange(0,100)))
print("el numero es", numOrdenador)
while True:
    numEntrada = input("ingrese un numero entero: ")

    if numEntrada.isdigit():
        numEntrada = int(numEntrada)
        break
    print("por favor ingrese solo numero positivos ")

while(numEntrada!=numOrdenador):

    if(numEntrada>numOrdenador):
        print("El numero a adivinar es menor")
    else:
        print("El numero a adivinar es mayor")
    while True:
        numEntrada= input("ingrese un nuevo numero: ")
        if numEntrada.isdigit():
            numEntrada = int(numEntrada)
            break
        print("ingrese solo numero")

print("Felicitaciones haz adivinado el numero")


""" .isdigit()  toma el - como un caracter, osea no hace nada con ese numero, no lo asigna"""
