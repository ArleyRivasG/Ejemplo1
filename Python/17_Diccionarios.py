""" En los dicionarios no hay posiciones, todo se accede por su clave"""


dict_1 ={"nombre": "Carlos",
         "edad": 22,
         "cursos": ["Python", "Java","Html"]}

print(type(dict_1))
print(dict_1)
""" accedemos por su llave o clave"""
print(dict_1["cursos"])
print(dict_1["cursos"][1])
print(dict_1["nombre"][3]) #imprime la L de carlos.

for key in dict_1:
    print(key, ":" , dict_1[key])


#Crear un diccionario a partir del metodo dic()
dict_2= dict(nombre="Ana", estatura=1.65, ocupacion="Estudiante")
print(type(dict_2))
print(dict_2)

# Zip: crear diccionario con el metodo Zip() zip("las n claves", "los n valores de las claves")
dict_3 = dict(zip("abcdef", [1,2,3,4,5,6]))
print(dict_3)

# Zip:los paramentros de zip pueden ser tuplas o listas  zip([],[]) o zip((),[])
dict_4 = dict(zip([10,20,30,40, 50, 60], [1,2,3,4,5,6]))
print(dict_4)

# items Extraer todo lo que tiene un diccionario queda de tipo dict_items
var_1 = dict_1.items()
print(var_1)
print(type(var_1))

#list() o tuple() para convertir un .items en listas o tuplas
var_2 = list(dict_2.items())
print(var_2)
print(type(var_2))

var_3 = tuple(dict_3.items())
print(var_3)
print(type(var_3))

# keys.() me trae todas las llaves del diccionario en tipo de dato dict_keys
var_1= dict_1.keys()
print(var_1)
print(type(var_1))

var_1= list(dict_1.keys())
print(var_1)
print(type(var_1))


var_3 = list(dict_3.values())
print(var_3)
print(type(var_3))

""" metodos:
 .clear() para vaciar todo el diccionario
 .copy() crear copia del diccionario
 .get() recibe la clave del elemento a extraer
 .pop() recibe la clave, para eliminar ese elemento (tanto su clave como su valor)
 .update() actualiza un diccionario de acuerdo a las claves del diccionario que recibe como parametro y agrega los que no existan por esa clave
"""

print(dict_1.get("nombre"))

dict_5 = { "a": 1,"b": 2, "c": 3 }
dict_6 = { "a": 4, "c": 5 , "d": 6}
dict_5.update(dict_6)
print(dict_5)


#Cambiar valores de forma directa usando su clave
dict_1["edad"]= 30
