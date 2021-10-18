"""la posicion 0 del vector describe el tamaño del vector, no se puede tocar"""
from Vector import Vector
import random

def capicua(numero):
    num_str= str(numero)
    list_num= list(num_str)
    list_rev = list_num.copy()
    list_rev.reverse()
    print(list_num)
    print(list_rev)
    if(list_num== list_rev):
        return True
    else:
        return False


capicua(51415)
def solucion():
    n= random.randit(15, 30)
    vec4 = vector(n)
    """al trabajar con el .V trabajamos con la lista que esta dentro del vector, 
    esto no modifica  al vector, solo trabajamos con sus datos en lista"""
    vec4.V[0]= n

    for x in range(1, n+1):
        vec4.V[x] = random.randint(1, 99999)
        print(vec4.V)
