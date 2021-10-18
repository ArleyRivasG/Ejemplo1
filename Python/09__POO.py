"""En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El banco requiere también
 al final del día calcular la cantidad de dinero que se ha depositado.
Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá
 los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total.

La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total."""

class Cliente():

    def __init__(self, nombre, cantidad=0):
        self.nombre = nombre
        self.cantidad = cantidad

    def depositar(self, cantidad):
        self.cantidad += cantidad

    def extraer(self, cantidad):
        self.cantidad -= cantidad

    def mostrar_total(self):
        print(self.nombre + ' Tiene un ahorro de: ' + str(self.cantidad))

    def retornar_cantidad(self):
        return self.cantidad

class Banco():

    def __init__(self):
        self.cliente_1 = Cliente('Raul', 10000)
        self.cliente_2 = Cliente('Fany', 20000)
        self.cliente_3 = Cliente('Sandra', 100000)

    def operar(self):
        self.cliente_1.depositar(5000)
        self.cliente_2.extraer(3000)
        self.cliente_3.depositar(10000)
        self.cliente_2.depositar(4000)
        self.cliente_1.extraer(6000)

    def deposito_total(self):
        total = self.cliente_1.retornar_cantidad() + self.cliente_2.retornar_cantidad() + self.cliente_3.retornar_cantidad()
        print('El dinero total en el  banco es:', total)





banco_1 = Banco()
banco_1.operar()
banco_1.deposito_total()
