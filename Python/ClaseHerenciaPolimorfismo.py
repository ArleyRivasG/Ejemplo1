"""class Animal:
    def __init__ (self, especie, edad):
        self.especie = especie
        self.edad=edad

    def hablar(self):
        print("Guau-guau")

    def moverse(self):
        # pass
        print("Camino en 4 patas")

    def describeme(self):
        print("Soy un animal del tipo", type(self).__name__)
        # pass

class Perro(Animal):
    pass

print(Perro.__bases__)

print(Animal.__subclasses__())

miPerro = Perro("Mamifero", 5 )
miPerro.describeme()
miPerro.hablar()
miPerro.moverse()"""


class Animal:
    def __init__ (self, especie, edad):
        self.especie = especie
        self.edad=edad

    def hablar(self):
        print("Guau-guau")
        print("Te dejo hablar como animal que eres")

    def moverse(self):
        # pass
        print("Camino en 4 patas")

    def describeme(self):
        print("Soy un animal del tipo", type(self).__name__)
        # pass

class Perro(Animal):
    def hablar(self):
        print("Guau-guau")

    def moverse(self):
        # pass
        print("Camino en 4 patas")


class Vaca(Animal):
    def hablar(self):
        print("Muuu")

    def moverse(self):
        # pass
        print("Camino en 4 patas")



class Abeja(Animal):
    def hablar(self):
        print("Bzzz")

    def moverse(self):
        # pass
        print("Volando")

        #nuevo metodo
    def picar(self):
        print("Te piquee!!")

#imprime a que clase pertenece Perro en este caso Animal
print(Perro.__bases__)

#imprime a quien heredo de Animal, en este caso, Perro, Vaca y Abeja.
print(Animal.__subclasses__())

miPerro = Perro("Mamifero", 5 )
miPerro.describeme()
miPerro.hablar()
miPerro.moverse()

miVaca = Vaca("Mamifero", 4)
miVaca.describeme()
miVaca.hablar()
miVaca.moverse()

miAbeja = Abeja("Insecto", 1)
miAbeja.describeme()
miAbeja.hablar()
miAbeja.moverse()
miAbeja.picar()
#miAbeja.super().__init__()
























