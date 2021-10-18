"""1. Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad e identificación.
Construye los siguientes métodos para la clase:
Un constructor. mostrar(): Muestra los datos de la persona.
esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad."""

class Persona:
    def __init__(self, nombre, edad, identificacion):
        self.nombre= nombre
        self.edad=edad
        self.identifacion= identificacion

    def mostrar(self):
        datos = "Nombre: " + self.nombre + ", Edad: " + str(self.edad) + ", Identificacion: " + str(self.identifacion)
        return datos
        """con la , muestro multiples datos y da un espacio, con el + todo lo vuelvo una cadena"""

    def esMayorEdad(self):
        return (self.edad >= 18)

persona = Persona("Carlos", 17, 1111642217)
print(persona.mostrar())
print(persona.esMayorEdad())


""" Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
Un constructor.
mostrar(): Muestra los datos de la cuenta.
ingresar(cantidad): Se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
retirar(cantidad): Se retira una cantidad a la cuenta. La cuenta puede estar en números rojos."""

class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        datos= "Titular: "+ self.titular + ", Cantidad: " + str(self.cantidad)
        if(self.cantidad <0):
            print("Ojo! Cuenta en rojo")
        return datos

    def ingresarCantidad(self, cantidad):
        if(cantidad>0):
            self.cantidad= self.cantidad + cantidad


    def retirar(self, cantidad):
        self.cantidad= self.cantidad-cantidad
        if(self.cantidad<0):
            return print("Pasates a tener deuda; tu cuenta esta en rojo")

#creo objeto cuenta de la clase Cuenta
cuenta = Cuenta("Arley Rivas", 1000)

cuenta.ingresarCantidad(8000)
print(cuenta.mostrar())
print(cuenta.retirar(1000.54))
print(cuenta.mostrar())
cuenta.ingresarCantidad(3000)
cuenta.mostrar()



