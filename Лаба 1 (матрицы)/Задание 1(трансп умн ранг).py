def printf(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print("")
    print("-------------")

stroka_1, stolb_1 = map(int, input("Введите количество строк и столбов через пробел для первой матрицы: ").split(" "))
matrix_1 = []
for i in range(stroka_1):
    matrix_1.append(list(map(int, input("Введите {0} элементов в {1} строке через пробел: ".format(stolb_1, i+1)).split(" "))))

stroka_2, stolb_2 = map(int, input("Введите количество строк и столбов через пробел для второй матрицы: ").split(" "))
matrix_2 = []
for i in range(stroka_2):
    matrix_2.append(list(map(int, input("Введите {0} элементов в {1} строке через пробел: ".format(stolb_2, i+1)).split(" "))))

print("Матрица 1\n")
printf(matrix_1)
print("Матрица 2\n")
printf(matrix_2)


# Транспонирование Матрицы 1
def transp(matrix_1, stroka_1, stolb_1):
    transp_matrix = [[0 for i in range(stroka_1)] for j in range(stolb_1)] # Итоговый массив, где количество строк
    # равно количеству столбцов и наоборот
    for j in range(stroka_1):
        for i in range(stolb_1):
            transp_matrix[i][j] = matrix_1[j][i] # Записываем на место элемент из [строки/столбца] [столбец/строку]
    return transp_matrix

print("Транспонированная Матрица 1:\n")
printf(transp(matrix_1, stroka_1, stolb_1))


# Умножение Матриц
def multi(matrix_1, matrix_2):
    multi_matrix = [[0 for i in range(stolb_2)] for j in range(stroka_1)]  # Создаём итоговый массив, удобный для умножения (заполняет нулями)
    matrix_2 = transp(matrix_2, stroka_2, stolb_2)
    for i in range(stroka_1):
        for j in range(stolb_2):
            for elem in range(stroka_2):
                multi_matrix[i][j] += matrix_1[i][elem] * matrix_2[j][elem]
    return multi_matrix

print("Умножение Матрицы 1 на 2:\n")
printf(multi(matrix_1, matrix_2))


#Определение ранга Матрицы 1
from itertools import *
def check(stroka_1,cnt):
    f=0
    alg=[s for s in permutations(range(1, stroka_1+1), stroka_1)]
    for l in range(len(alg)):
        b=0
        for i in range(stroka_1-1):
            for j in range(i+1, stroka_1):
                b+=alg[l][i]>alg[l][j]
        c=(-1)**l
        for u in range(stroka_1):
            c*=cnt[u][alg[l][u]-1]
        f+=c
    return f


def ranks(stroka_1,stolb_1,cnt):
    for n in range(min(stroka_1,stolb_1),0,-1): #границы квадрата <=mix(x,y)
        for i in range(stolb_1-n+1):
            for j in range(stroka_1-n+1): #проверка миноров
                list = [[[] for _ in range(n)] for _ in range(n)]
                for l in range(i,i+n):
                    for u in range(j,j+n): #проверка не соседних миноров
                        list[u-j][l-i]=cnt[u][l]
                if check(len(list),list)!=0: # Проходимся по строкам, чтобы найти первое ненулевое значение
                    return n
print("Ранг Матрицы 1:\n")
print(ranks(stroka_1, stolb_1, matrix_1))