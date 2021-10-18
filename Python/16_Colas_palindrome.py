class Cola:
    def __init__(self):
        self.cola=[]

    def push(self, data):
        self.cola.append(data)


    def isEmpty (sefl):
        if len(sefl.cola)==0:
            return  True
        else:
            return False

    def pop (self):
        if self.isEmpty():
            return None
        else:
            data =self.cola.pop(0)
            return data

    def front(self):
        if len(self.cola)==0:
            return None
        else:
            return self.cola[0]

    def primerElemento (self):
        if self.isEmpty():
            return self.cola[-1]
        else:
            return None

    def tamaño (self):
        return len(self.cola)

    def imprimirUnoUno (self):
        if (len(self.cola)==0):
            print("Cola Vacia")
        else:
            for i in range(len(self.cola)):
                print(self.cola[i], end=", ")
            print("\n")





def palindromo(texto):
    parteInicial = Cola()
    parteFinal = Cola()
    texto = texto.lower()
    texto = texto.replace(' ', '')


    mitad = len(texto) // 2
    indiceFinal= len(texto)-1

    for i in range(mitad):
        parteInicial.push(texto[i])
        parteFinal.push(texto[indiceFinal])
        indiceFinal -= 1
        print(parteInicial.imprimirUnoUno(), parteFinal.imprimirUnoUno()) #solo para ver su comportamiento(puedo borrar esta linea)

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

