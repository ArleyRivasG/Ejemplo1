"""Definir la clase Figuras con un método area, y a partir de esta generar las cases derivadas:
Rectángulo
Círculo
Triángulo
Cada una con su respectivo constructor y los métodos redefinidos de area."""

from math import pi

class Figuras():

    def area (self):
      pass


class Circulo(Figuras):

        def __init__(self, radio=0):
            self.radio = radio
        def areaHijoCir(self):
            return ("El area del Circulo es: " + str(pi * self.radio**2))

class Triangulo(Figuras):

        def __init__(self, base, altura):
            self.base = base
            self.altura = altura

        def areaHijoTria(self):
            return ("El area del Triángulo es: " + str((self.base * self.altura / 2)))

class Rectangulo(Figuras):

        def __init__(self, base, altura):
            self.base = base
            self.altura = altura

        def areaHijoRetan(self):
            return ("El area del Rectángulo es: " + str(self.base * self.altura ))


circulo = Circulo(100)
print(circulo.areaHijoCir())

rectangulo = Rectangulo(7, 12)
print(rectangulo.areaHijoRetan())

triangulo = Triangulo(4, 8)
print(triangulo.areaHijoTria())



""" SOLUCIÓN WILBERT 
from math import pi

class Figura:
    def setArea(self, area):
        self.area= area

class rectangulo(Figura):
    def __init__(self, base, altura):
        self.base=base
        self.altura= altura
    def setArea(self):
        return self.base * self.altura

class circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def setArea(self):
        return pi * self.radio ** 2


class triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def setArea(self):
        return (self.base * self.altura)/2

mi_triangulo= triangulo(18,3)
print(mi_triangulo.setArea())

mi_rectangulo= rectangulo(18,3)
print(mi_rectangulo.setArea())


mi_circulo= circulo(100)
print(mi_circulo.setArea())



"""

""" 2. Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos:
Inicializar los atributos por teclado utilizando el método __init__
Imprimir los valores de los lados
Imprimir el o los valores de los lado con el tamaño mayor
Imprimir el tipo de triángulo: equilátero, isósceles o escaleno. """

class Triangulo:

  def __init__(self):
    self.lado_1 = int(input('Ingrese lado 1: '))
    self.lado_2 = int(input('Ingrese lado 2: '))
    self.lado_3 = int(input('Ingrese lado 3: '))

  def imprimir(self):
    print('Los lados ingresados son:')
    print('Lado 1:', self.lado_1)
    print('Lado 2:', self.lado_2)
    print('Lado 3:', self.lado_3)

  def mayor(self):
    list_lados = [self.lado_1, self.lado_2, self.lado_3]
    #list_lados.sort()
    return max(list_lados)

  def tipo_tri(self):
    if self.lado_1 == self.lado_2 and self.lado_1 == self.lado_3:
      tipo = "Equilátero"
    elif self.lado_1 != self.lado_2 and self.lado_1 != self.lado_3 and self.lado_2 != self.lado_3:
      tipo = "Escaleno"
    else:
      tipo = "Isósceles"
    return tipo

tri = Triangulo()
tri.imprimir()
print('El lado mayor es:', tri.mayor())
print("El triángulo es tipo:", tri.tipo_tri())


