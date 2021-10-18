""" Sctak es Pila"""

class Stack:
    def __init__(self):
        self.pila=[]

    def push(self, data):
        self.pila.append(data)

    def pop(self):
        self.data = self.pila.pop()
        """poc() sin argumento elimina el ultimo valor es lo mismo que en las listas"""

    #si esta vacia
    def isEmpty(self):
        return len(self.pila) == 0
    #el tamaño
    def length (self):
        return len(self.pila)

    def top (self):
        if self.isEmpty():
            return None
        else:
            return self.pila[-1]

    def print_pila(self):
        for i in range (len(self.pila)):
            print(self.pila[i])

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

 #codigo del profesor
"""class Stack:
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
"""


# Palíndromo
# Yo hago yoga hoy -> yohagoyogahoy
"""
def palindromo(texto):
    p = Stack()
    texto = texto.lower()
    texto = texto.replace(' ', '')
    texto = texto.replace(',', '')#eliminar solo los elementos que si se que estan en el texto, sino me marca error

    mitad = len(texto) // 2

    for i in range(mitad):
        p.push(texto[i])

    isPalind = True

    if len(texto) % 2 != 0:
        i = mitad + 1
    else:
        i = mitad

    while not p.isEmpty() and isPalind:
        caracter = p.pop()
        if texto[i] != caracter:
            isPalind = False
        i += 1

    if isPalind == True:
        print('SI es Palíndromo')
    else:
        print('NO es Palíndromo')


a = 'Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, de panico camina, onice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nomina y animo de mortecina, ya ni giros elimina, ya ni poeta, ya ni vida '
palindromo(a)
"""


# Palíndromo
# Yo hago yoga hoy -> yohagoyogahoy
def palindromo(texto):
    parteInicial = Stack()
    parteFinal=Stack()
    texto = texto.lower()
    texto = texto.replace(' ', '')


    mitad = len(texto) // 2
    indiceFinal= len(texto)-1

    for i in range(mitad):
        parteInicial.push(texto[i])
        parteFinal.push(texto[indiceFinal])
        indiceFinal -= 1
        print(parteInicial.print_pila(), parteFinal.print_pila())

    #if (parteInicial.print_pila()==partFinal.print_pila()):
     #   print("Es Palindromo")

    #else:
     #   print("No es Palindromo")

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

cadena="a2ca ytaffsdfsdf2a"
palindromo(cadena)