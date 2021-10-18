
"""while True:
        numeroPrimo = input("ingrese el numero entero a evaluar si es primo: ")
        if numeroPrimo.isdigit() is True:
            numeroPrimo= int(numeroPrimo)
            break
        print("por favor ingrese solo numero entero positivo")
i=1
contador=0
while (i <= numeroPrimo):

    if numeroPrimo % i == 0:
        contador=contador+1

    i+=1

if(contador==2):
    print(f'el numero: {numeroPrimo} es primo')
else:
    print(f'el numero {numeroPrimo} no es primo')"""


"""cont=0
while (cont <= 10):
    print(round(cont))
    cont += 0.1 """


"""Segunda opción más eficiente para conocer un NÚMERO PRIMO"""

# pedimos el numero y rompemos el while solo cuando ingresen un numero y a su vez sea mayor que 0
while True:
    numeroPrimo = input("ingrese el numero entero a evaluar si es primo: ")

    if numeroPrimo.isdigit() is True:
        numeroPrimo = int(numeroPrimo)
        if (numeroPrimo != 0):
            break
        print("por favor ingrese solo numero entero positivo ")

# aumento i de entrada vale 2 ya que 1 siempre tiene residuo 0 (ahorro una iterración
i = 2
contador2 = 0

while (i < numeroPrimo):

    if numeroPrimo % i == 0:
        contador2 = contador2 + 1

    i = i + 1
    # si ya encuentra un numero que de residuo 0 aparte de 1 y el mismo numero ya no es # primo
    if (contador2 > 0):
        break

print(contador2)
# si encuentra un divisor exacto ya no es primo
if (contador2 > 0 or numeroPrimo == 1):
    print(f'el numero: {numeroPrimo} no es primo')
elif (contador2 == 0):
    print(f'el numero {numeroPrimo} es primo')
