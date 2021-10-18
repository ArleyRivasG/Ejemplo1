import numpy as np

# NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
# LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

# En este espacio podrás programar las funciones que deseas usar en la función solución (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)
"""Inicio espacio para programar funciones propias"""

# PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES


"""Fin espacio para programar funciones propias"""


def solucionMenor_Posiciones(matriz):
    matrizABuscar = np.copy(matriz) #por si no viene en matriz
    numMenor= matrizABuscar[0,1]
    tuplaPosicMenor = []

    for fila in range (len(matrizABuscar)):
        for column in range(len(matrizABuscar)-fila):


            if(((column - fila) % 2) != 0):
                if(((numMenor == (matrizABuscar[fila,column])))):
                    tuplaPosicMenor.append((fila, column))
                if(numMenor > (matrizABuscar[fila,column])):
                    numMenor = matrizABuscar[fila,column]
                    tuplaPosicMenor = []
                    tuplaPosicMenor.append((fila, column))



    return numMenor, tuplaPosicMenor



list_1 = [[0,1,3,6,4],[4,5,6,5,1], [23,10,7,8,5], [1, 4, 7, 8,2]]
mat_1 = np.array(list_1)
print(list_1 , "\n" , mat_1)

matriz_entrada = np.array([[89, 5, 23, 10],
                           [10, 5, 8, 62],
                           [27, 10, 88, 33],
                           [ 5, 78, 5, -11]])

print("\n", matriz_entrada)
salida=(solucionMenor_Posiciones(matriz_entrada)) #~Funciona bien, devuelve el menor encontrado
print(salida[0])
print(salida[1])
# falta decirle que solo los de la diagonal hacia arriba,
# toca sacar las posiciones donde se encuentra y meterlo en una tupla



