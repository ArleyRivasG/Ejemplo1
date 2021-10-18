class Cuenta():

    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        cadena = "Cuenta = " + "Titular: " + self.titular + " - Cantidad: " + str(self.cantidad)
        return cadena

    def esMayorDeEdad(self):
        return self.edad >= 18

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad = self.cantidad + cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad = self.cantidad - cantidad


"""     3. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la anterior.
 Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto
  por ciento.Construye los siguientes métodos para la clase:
Un constructor.
En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
Además la retirada de dinero sólo se podrá hacer si el titular es válido.
Piensa los métodos heredados de la clase madre que hay que reescribir.
            """


class CuentaJoven(Cuenta):

    def __init__(self, titular, edad, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
        self.edad = edad

    def mostrar(self):
        cadena = "Cuenta Joven = " + "Titular: " + self.titular + " - Edad: " + str(self.edad) + " - Cantidad: " + str(
            self.cantidad) + "- Bonificación: " + str(self.bonificacion) + "%"
        return cadena

    def esTitularValido(self):
        return self.edad < 25 and self.esMayorDeEdad()

    def retirar(self, cantidad):
        if not self.esTitularValido():
            print("No puedes retirar el dinero. titular no válido")
        elif cantidad > 0:
            super().retirar(cantidad)


M = CuentaJoven('Moncayo', 13, 10000000, 0.2)
print(M.mostrar())
print(M.esTitularValido())
M.retirar(250000)
