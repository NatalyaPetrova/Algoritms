import numpy as np
stroka_1, stolb_1 = map(int, input("Введите количество строк и столбов через пробел для первой матрицы: ").split(" "))
matrix_1 = []
for i in range(stroka_1):
    matrix_1.append(list(map(int, input("Введите {0} элементов в {1} строке через пробел: ".format(stolb_1, i+1)).split(" "))))
stroka_2, stolb_2 = map(int, input("Введите количество строк и столбов через пробел для второй матрицы: ").split(" "))
matrix_2 = []
for i in range(stroka_2):
    matrix_2.append(list(map(int, input("Введите {0} элементов в {1} строке через пробел: ".format(stolb_2, i+1)).split(" "))))

arr_transpose=np.transpose(matrix_1)
arr_multi=np.dot(matrix_1,matrix_2)
arr_rank=np.linalg.matrix_rank(matrix_1)
print()
print('Транспонированная Матрица 1:')
print(arr_transpose)
print()
print('Умножение Матрицы 1 на 2:')
print(arr_multi)
print()
print('Ранг Матрицы 1:')
print(arr_rank)
