nombre= "Arley"
print("¡Hola " + nombre + "!")

p1 = float(input("ingrese la nota de la practica 1: "))
p2 = float(input("ingrese la nota de la practica 2: "))
p3 = float(input("ingrese la nota de la practica 3: "))

ep = float(input("ingrese la nota del examen parcial: "))
ef = float(input("ingrese la nota del examen final: "))

pp = float((p1 +p2 +p3 )/ 3)
prom = float((pp + (2 * ep) + (3 * ef))/6)
print(f"la nota promedio del alumno es: {prom}")