import random

matriz=[[1,2,3],[4,5,6,7]]

print("matriz sin usar np.array (matriz)")
print(matriz)




def crear_matriz(n, m):
    matriz = []
    for row in range(n):
         fila = []
         for col in range(m):
            fila.append(random.randint(1, 50))
            matriz.append(fila)
    return matriz

mat = crear_matriz(2, 3)

for y in mat:
    print(y)

""""Segunda parte Matriz presentación"""
import numpy as np

list_1 = [[1,2,3,6],[4,5,6,5], [23,10,7,0]]
mat_1 = np.array(list_1)


print('Matriz Original')
print(mat_1)

print('Matriz Copia * 5')
mat_c = np.copy(mat_1*5)
print(mat_c)

print('Extrae (23) extrae el numero de la posicíon')
print(mat_1[2, 0])

mat_1[1,2] = 11
print(mat_1)

print('Matriz sumando 8')
print(mat_1+8)

print('Sumando 2 Matries')
mat_sum = mat_1+mat_c
print(mat_sum)


list_1 = [[1,2,3,6],[4,5,6,5], [23,10,7,0], [2, 4, 7, 8]]
mat_1 = np.array(list_1)

print('Matriz Original')
print(mat_1)

print('Cambiando Filas')
print(mat_1[[2,1,0],:])

print('Cambiando Columnas')
print(mat_1[:,[2, 1, 0, 3]])

print('Matriz Transpuesta')
print(np.transpose(mat_1))

print('Matriz Triangular Inferior:')
print(np.tril(mat_1))

print('Matriz Triangular Inferior Estricta:')
print(np.tril(mat_1, -1))

print('Matriz Triangular Superior:')
print(np.triu(mat_1))

print('Matriz Triangular Superior Estricta:')
print(np.triu(mat_1, 1))

