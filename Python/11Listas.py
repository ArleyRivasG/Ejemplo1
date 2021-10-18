lista= ["ana", "paco", "andres", "juan"]
lista2 = [1, 2, 3, 4, 5]
lista3 = ["ana", "paco", 1, 2, 3, 4, 5]
print(lista)
lista.sort()
print(lista)
lista_copia = lista.copy()
lista.sort(reverse=True)
print(lista)
print(lista_copia)

lista_num = []
lista2_string = []

for x in lista3:
    print("dato: ", x)
    if(type(x) == int):
        print("es entero")
    elif(type(x) == str):
        print("es cadena")
""" 
.pop() elimina de acuerdo a la posición como parametro 

.reverse() imprime invertido
.sort() los ordena de menor a mayor 

"""
list_1 = ['ana', 'juan', 'paco', 'hugo', 'luis']
list_2 = [1, 5, 7, 9, 43, 89]
String = delimiter.join(lista_1)
print(sum(list_2))