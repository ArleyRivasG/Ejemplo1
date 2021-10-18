edad= int(input("ingrese su edad: "))

if edad<18:
  print("Eres menor de edad.")
else:
  print("Eres mayor de edad.")





# Menor o igual que 10, Talla s
# Mayor que 10 y menor o igual a 20, Talla M
# Mayor que 20, Talla L

talla = int(input("ingrese su talla: "))

if talla <= 10:
    print("Talla S")
elif talla > 10 and talla <= 20:  # o poner (10 < talla <= 20)
    print("Talla M")
else:
    print("Talla L")

# Menor o igual que 10, Talla s
# Mayor que 10 y menor o igual a 20, Talla M
#   Si talla es menor o igual a 15, talla M1
#   si talla esta entre 16 y 20 talla M2
# Mayor que 20 y menor o igual a 30 Talla L
# Mayor a 30 fuera de rango


"""Crea un programa que calcule el equivalente humano de la edad de un perro. 
Los dos primeros años de vida de un perro equivalen cada uno a diez y medio años humanos,
 y los siguientes años de vida de un perro equivalen cada uno a cuatro años humanos.
[14]"""

edad = int(input("Ingrese la edad del perro: "))

if (edad <= 2):
    print("La edad del perro equivalente a edad humana es: ", edad * 10.5, "años")
else:
    print("La edad del perro equivalente a edad humana es: ", ((2 * 10.5) + ((edad - 2) * 4)))



""" 4. Escribir un programa que pida tres números y 
diga si el tercero está más cerca del primero o del segundo."""

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

dif1= abs(num1-num3)
dif2= abs(num2-num3)

if (dif1<dif2):
  print(f"el tercer numero: {num3} esta más cerca al primer numero: {num1} que al segundo {num2}")
elif (dif2<dif1):
  print(f"el tercer numero: {num3} esta más cerca al segundo numero: {num2} que al primero {num1}")
else:
   print(f"el tercer numero: {num3} esta igual de cerca al segundo numero: {num2} que al primero {num1}")


""" 5. Crear un programa que permita al usuario elegir un candidato por el cual votar.
 Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde,
  candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir 
  el mensaje “Usted ha votado por el partido (color que corresponda al candidato elegido)”. 
  Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles,
   indicar “Opción errónea”."""


candidato= input("ingrese el candidato a votar (A, B ó C): ")
if (candidato =="candidato A"):
  print("usted ha votado por el partido rojo")
elif (candidato == "candidato B"):
  print("usted ha votado por el partido verde")
elif (candidato == "candidato C"):
  print("usted ha votado por el partido azul")
else:
  print("Opción errónea")




  """ CICLO WHILE"""

numero= int(input("ingrese un numero"))
while numero!=0:
    numero = int(input("ingrese un numero: "))

cont=0
while(cont <= 10):
    print(cont)
    if(cont==5):
        break
    cont += 1


