"""contraseña1= input("please ingrese la contraseña: ")
contraseña2= input("please repita la contraseña: ")
cont= 1
while contraseña1 != contraseña2:
  if (cont<3):
    contraseña1 = input("contraseña no coincide, please repita la contraseña: ")
    contraseña2= input("please repita la contraseña: ")
    cont += 1
  elif ( contraseña1 == contraseña2):

    break

  print("contraseña incorrecta")

if ( contraseña1 == contraseña2):
  print("contraseñas iguales")"""


# Leer números enteros de teclado, hasta que el usuario ingrese el 0.
# Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

# pedimos el numero y rompemos el while solo cuando ingresen un numero y a su vez sea mayor que 0

while True:
  numEntrada = input("ingrese un numero entero: ")
  num22=int(numEntrada)

  if num22<0 or numEntrada.isdigit():
    numEntrada = int(numEntrada)
    break
  print("por favor ingrese solo numero o 0 para finalizar")

sumaEntero = 0
while (numEntrada != 0):
  sumaEntero = sumaEntero + numEntrada
  while True:
    numEntrada = input("ingrese el numero entero: ")
    num22 = int(numEntrada)
    if num22<0 or numEntrada.isdigit():
      numEntrada = int(numEntrada)
      break
    print("por favor ingrese solo numero o 0 para finalizar")

print("La suma de los numeros es:", sumaEntero)
