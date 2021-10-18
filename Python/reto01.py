"""Escriba un programa en Python que lea dos nombres, luego usando esos nombres lea los apellidos correspondientes
y por último imprima los nombres con sus respectivos apellidos en una sola línea.
Ejemplo:

Entradas:
    Mateo
    Sofía
    Rivera
    Vanegas

Salida:     Mateo Rivera Sofía Vanegas"""

nom1 = str(input("Ingrese el primer nombre: "))
nom2 = str(input("Ingrese el segundo nombre: "))
print("Ingrese el apellido de ", nom1, ": ")
apellido1 = str(input())
print("Ingrese el apellido de", nom2, ": ")
apellido2 = str(input())

print(nom1, " ", apellido1, " ", nom2, " ", apellido2)
