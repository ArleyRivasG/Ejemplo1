import random

numOrdenador=int((random.randrange(0,100)))
print("el numero es", numOrdenador)

while True:
    try:
        numEntrada = int(input("ingrese un numero: "))
        break
    except:
        print("ERROR: Debe ingresar solo numeros")

while (numOrdenador != numEntrada):
    while True:
        try:
            numEntrada = int(input("ingrese un numero: "))
            break
        except:
            print("ERROR: Debe ingresar solo numeros")

    if (numEntrada > numOrdenador):
        print("El numero a adivinar es menor.")
    else:
        print("El numero a adivinar es mayor.")


print("Felicitaciones haz adivinado el numero")