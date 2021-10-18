""" 1. Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje:
[nombre] tiene [edad] años, vive en [dirección] y su número de teléfono es [teléfono]."""

nombre = input('Ingresa nombre: ')
edad = int(input('Ingresa edad: '))
dir = input('Ingresa direccion: ')
tel = int(input('Ingresa telefono: '))

persona ={'nombre': nombre, 'edad': edad, 'direccion': dir, 'telefono': tel}

print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'],
      'y su número de teléfono es', persona['telefono'])


""" #2
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio
de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello."""

dic_frutas = {"Platano": 1.35, "Manzana": 0.80, "Pera":0.85 , "Naranja":0.70}

calcular = "si"
while calcular=="si":
    fruta= input("ingrese la fruta: ")
    cantidad=int(input("ingrese el precio de la fruta: "))

    if(fruta in dic_frutas):
        precio= dic_frutas[fruta]
        print(precio)
        valor =precio * cantidad
        print( "el valor de " , cantidad, "kilos de", fruta, "es $", valor,)
    else:
        print("Fruta no encontrada")

    calcular= input("Desea calcular otro precio? (si\no): ")




"""#3 Escribir un programa que cree un diccionario vacío 
y lo vaya llenado con información sobre una persona
 (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe 
imprimirse el contenido del diccionario."""

dict_persona = {}

continuar = input('Desea ingresar un dato?(si/no):')

while continuar == 'si':
  clave = input('Ingrese categoría: ')
  valor = input('Ingerese su valor: ')
  dict_persona[clave] = valor
  print(dict_persona)
  continuar = input('Desea ingresar un dato?(si/no):')

print(dict_persona)


"""4. Escribe un programa python que pida un número por teclado y que cree 
un diccionario cuyas claves sean desde el número 1 hasta el 
número indicado, y los valores sean los cuadrados de las claves. """




"""5 Escribe un programa que lea una cadena y devuelva un diccionario con la 
cantidad de apariciones de cada carácter en la cadena."""

cadena = 'esternocleidomastoideo' # OTORRINOLARINGOLOGO
dict_palabra= {}

for x in cadena:
  if x in dict_palabra:
    continue
  else:
    dict_palabra[x] = cadena.count(x)

print(dict_palabra)


# hacer ejercicios 2 y  4 de Diccionario y leer presentación libreria