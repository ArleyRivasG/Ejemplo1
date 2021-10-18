
while True:
    try:
        numero = int(input("Escriba un numero de 4 digitos: "))
        if (numero >= -9999 and numero <= -1000) or (numero >= 1000 and numero <= 9999):
            break
        else:
            print("Error! el numero es invalido, recuerde que el numero debe tener 4 digitos")
    except:
        print("Error! solo puedes ingresar numeros: ")




num_str= str(numero)
suma=0
if(numero<0):
    for x in range(1, 5):
        print(num_str[x])
        suma +=int(num_str[x])
else:
    for x in range(0, 4):
        print(num_str[x])
        suma +=int(num_str[x])
print("la suma de digitos es: ", suma)

