"""Realiza una función llamada area_rectangulo(base, altura)
que devuelva el área del rectangulo a partir de una base y una altura.
Calcula el área de un rectángulo de 15 de base y 10 de altura:"""


def area_rectangulo(base, altura):
    area = base * altura
    return area


calcuArea = area_rectangulo(15, 10)
print(calcuArea)


def area_rectangulo2(base, altura):
    area = base * altura
    print("el area es: ", area)


area_rectangulo2(8, 7)

"""Realiza una función llamada area_circulo(radio) 
que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio."""

"""Realiza una función llamada area_rectangulo(base, altura)
que devuelva el área del rectangulo  y su perimetro a partir de una base y una altura.
Calcula el área de un rectángulo de 15 de base y 10 de altura:"""

def area_rectangulo3(base, altura):
    area = base * altura
    perimetro = 2*base + 2*altura
    return area, perimetro


calcuArea, calcuPerimetro = area_rectangulo3(15, 10)
print("El area es: ",calcuArea)
print("El perimetro es: ",calcuPerimetro)


def area_rectangulo4(base, altura):
    area = base * altura
    perimetro = 2*base + 2*altura
    return area, perimetro

base = float(input("ingrese la base: "))
altura = float(input("ingrese la altura: "))

calcuArea, calcuPerimetro = area_rectangulo4(base, altura)
print("El area es: ",calcuArea)
print("El perimetro es: ",calcuPerimetro)



"""imprimir la fecha"""

import  datetime

def imprimirFecha ():
    fecha= datetime.datetime.now()
    print("la fecha actual es: ", fecha)


imprimirFecha()

"""3. Realizar un programa que calcule el área de 4 figuras geométricas."""

def cuadrado(lado):
    return lado**2

def triangulo(base, altura):
    return (base * altura) /2

def rectangulo(base, altura):
    return base * altura

#apotena es la distancia mas corta del centro a uno de sus lados
def pentagono(perimetro, apotena):
    return perimetro*apotena/2

def menu():
    print("MENÚ:")
    print("1. Cuadrado")
    print("2. Triangulo")
    print("3. Rectangulo")
    print("4. Pentagono")
    print("5. Salir")


menu()
opcion=int(input("ingrese opcion: "))

while opcion!=5:

    if opcion == 1:
        lado = float(input("ingrese lado: "))
        print("el area del Cuadrado es: " , cuadrado(lado))

    elif opcion == 2:
        base = float(input("ingrese base: "))
        altura = float(input("ingrese altura: "))
        print("el area del triangulo es: " , triangulo(base, altura))

    elif opcion == 3:
            base = float(input("ingrese base: "))
            altura = float(input("ingrese altura: "))
            print("el area del rectangulo es: ", triangulo(base, altura))

    elif opcion == 4:
            perimetro = float(input("ingrese perimetro: "))
            apotena = float(input("ingrese apotena: "))
            print("el area del pentagono es: ", pentagono(perimetro, apotena))
    else:
        print("Opcion Erronea!")

    menu()
    opcion = int(input("ingrese opcion: "))



"""Implementar un programa calculadora con 5 operaciones básicas:
 Sumar, restar, multiplicar, dividir y exponencial.
 El programa finaliza mediante opción del menú"""


