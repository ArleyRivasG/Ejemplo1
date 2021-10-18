while True:
    try:
        numero= int(input("ingrese un numero"))
        break
    except:
        print("Debe ingresar solo numeros")

factorial=1;
for i in range(1, numero+1):
    factorial= factorial * i

print("El factorial de ", numero, "es: " , factorial)


#con el continue salto las lineas que estan dentro del ciclo ejemplo

variable= 10
while variable > 0:
    variable -=1
    if variable == 5:
        continue
    print(variable)

#////////////// FOR
for i in range (3):
    print(i)
# el rango(comienzo, parada-1)
for i in range (5, 8):
    print(i)

#comienzo en 1 hasta 10 y doy saltos de 2 en 2
for i in range (1, 10, 2):
    print(i)

print("////////////////////////////////////////")
for i in range (10, 1, -2):
    print(i)



#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
