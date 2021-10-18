class Stack:
    def __init__(self):
        self.lista = []

    def push(self, data):
        self.lista.append(data)

    def pop(self):
        data = self.lista.pop()
        return data

    def isEmpty(self):
        return len(self.lista) == 0

    def length(self):
        return len(self.lista)

    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.lista[-1]

    def print_pila(self):
        for i in range(len(self.lista)):
            print(self.lista[i], end=', ')
        print('\n')


lis = Stack()
print('isEmpty:', lis.isEmpty())
print('push: 1')
lis.push(1)
lis.push(10)
lis.push(15)
lis.push(20)
lis.push(25)
print('lenght:', lis.length())
print('top:', lis.top())
lis.print_pila()
lis.pop()
lis.print_pila()


# Palíndromo
# Yo hago yoga hoy -> yohagoyogahoy
def palindromo(texto):
    parteInicial = Stack()
    parteFinal = Stack()
    texto = texto.lower()
    texto = texto.replace(' ', '')


    mitad = len(texto) // 2
    indiceFinal= len(texto)-1

    for i in range(mitad):
        parteInicial.push(texto[i])
        parteFinal.push(texto[indiceFinal])
        indiceFinal -= 1
        print(parteInicial.print_pila(), parteFinal.print_pila()) #solo para ver su comportamiento(puedo borrar esta linea)

    #procedemos a sacar cada letra y compararlas
    cont = 0
    while not parteInicial.isEmpty():
          letra1= parteInicial.pop()
          letra2= parteFinal.pop()
          if (letra1==letra2):
              cont += 1

    if (cont == mitad):
        print("Es Palindromo")
    else:
         print("No es Palindromo")

cadena="Alli ves Sevilla"
palindromo(cadena)


def palindromo2(texto):
    parteInicial = Stack()
    parteFinal = Stack()
    texto = texto.lower()
    texto = texto.replace(' ', '')

    mitad = len(texto) // 2
    indiceFinal = len(texto) - 1
    cont = 0
    for i in range(mitad):
        parteInicial.push(texto[i])
        parteFinal.push(texto[indiceFinal])
        indiceFinal -= 1
        print(parteInicial.print_pila(), parteFinal.print_pila()) #solo para ver su comportamiento(puedo borrar esta linea)
        if (parteInicial.pop() == parteFinal.pop()):
            cont += 1

    # if (parteInicial.print_pila()==partFinal.print_pila()):
    #   print("Es Palindromo")

    # else:
    #   print("No es Palindromo")

    if (cont == mitad):
        print("Es Palindromo")
    else:
        print("No es Palindromo")


cadena = "Alli ves f Sevilla"
print(cadena)
palindromo2(cadena)


#cuando imprime none se refiere a la .base Ejemplo explicaciòn: https://www.w3schools.com/python/numpy/numpy_copy_vs_view.asp

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)
