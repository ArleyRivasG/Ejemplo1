"""numero1= int(input("Ingrese el primer numero"))
numero2= int(input("ingrese el segundo numero"))

if (int(numero1) % int(numero2)==0):
    print (f' El numero{numero1} es multiplo de: {numero2} ')

else:
    print(f'el numero {numero1} no es multiplo de: {numero2}')"""
#numero1=""
while True:
        numero1 = input("Ingrese el primer numero entero: ")
        if numero1.isdigit() is True:
            numero1= int(numero1)
            break
        print("por favor ingrese solo numero entero")
#numero2=""
while True:
        numero2 = input(f"Ya tienes el numero {numero1} Ingrese el segundo numero entero: ")
        if numero2.isdigit() is True:
            numero2= int(numero2)
            break
        print("por favor ingrese solo numero entero")


if(numero1 % numero2 == 0):
    print(f'El numero: {numero2} es multiplo de {numero1}')
else:
    print(f' El numero: {numero2} no es multiplo de {numero1}')
#print(numero2)


""""
while True:
          variable_a_usar = input("Ingrese número entero: ")
          if variable_a_usar.isdigit() is True:
            variable_a_usar = int(variable_a_usar)
            break
        print("El número es %d" % (variable_a_usar))"""