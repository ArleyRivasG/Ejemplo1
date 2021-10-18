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





opcion = 0
cola= Cola()
while (opcion != 4):
    print("MENU:  opciones")
    print("opc 1. agregar al pacientes")
    print("opc 2. Llamar al pacientes")
    print("opc 3. listar al pacientes")
    print("opc 4. Finalizar jornada")

    opcion = int(input("seleccione una opción: "))

    if(opcion == 1):
        paciente = input("ingrese un paciente a la cola de espera: ")
        cola.push(paciente)

    if(opcion == 2):
        print("ya se llamo al paciente",   cola.pop() , "¿que sigue?")

    if(opcion == 3):
        cola.imprimirUnoUno()

    if(opcion == 4):
        print("Jornada finalizada")
    else: print("Opción Invalida")




