"""1. Escribir un programa que pregunte al usuario su edad y muestre por pantalla
todos los años que ha cumplido (desde 1 hasta su edad)."""
while True:
    try:
        edad= int(input("Ingrese su edad: "))
        break

    except:
        print("Error al ingresar la edad")

print("los años cumplidos son: ")

for i in range (1, edad+1, 1):
    print ("ano", i)



"""2. Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla todos los números impares desde 1 hasta ese número."""

while True:
    try:
        numero2= int(input("Ingrese un numero entero positivo: "))
        break
    except:
        print("Error! ingrese solo numeros")
print("los numeros impares desde 1 hasta ", numero2, " son:")
for i in range (1, numero2+1, 1):
    if (i%2!=0):
        print(i)


"""Escribir un programa que pida al usuario un número entero y muestre por 
pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido."""

while True:
    try:
        numero3= int(input("Ingrese un numero entero positivo: "))
        break
    except:
        print("Error! ingrese solo numeros")
for i in range (1, numero3+1 , 1):
    print("*"*i)
