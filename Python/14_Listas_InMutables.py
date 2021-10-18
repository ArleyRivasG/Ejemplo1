"""todo lo que sea () es tupla, lo que sea []  es lista"""

tupla = (1, 4, 5 , 1.7, "Reinaldo")
lista=[1, 4, 5, 1.7, "Raul" ]
print(tupla[3])
print(tupla)
print(lista)
list_tupl=[(1,3),(2,4),(5,5)]

print(list_tupl)

list_1= list(tupla)

print(type(tupla))
print(tupla)
print(list_1)

list_1.append("carlos")
tupla_1=tuple(list_1)
print(list_1)
print(tupla_1)
print(tupla_1.count(4))
print(tupla_1.__len__())