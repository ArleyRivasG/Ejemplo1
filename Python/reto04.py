"""Elabore programa en Python que le permita al usuario ingresar números enteros de
 manera indefinida, hasta que ingrese un número negativo, y al final imprimir la suma de los
números enteros pares sin incluir el número negativo en la suma."""

suma=0;
numero=0;
while True:
    try:
        numero = int(input("Escriba el numeros enteros a sumar, o uno negativo para detenerse: "))
        if (numero >= 0 and numero%2==0):
           suma += numero
        elif (numero<0):
            break
    except:
        print("Error! solo puedes ingresar numeros: ")

print("la suma de los numeros pares es: ", suma)
