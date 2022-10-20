print("Введите строки матрицы 3x3 (через Enter), указывая все элементы через пробел: ")
a = [[int(i) for i in input().split()] for _ in range(3)]

def determinant3x3(a): # Детерминант матрицы 3x3
    main_diag = a[0][0] * a[1][1] * a[2][2] + a[0][1] * a[1][2] * a[2][0] + a[1][0] * a[2][1] * a[0][2]
    pob_diag = a[2][0] * a[1][1] * a[0][2] + a[1][0] * a[0][1] * a[2][2] + a[2][1] * a[1][2] * a[0][0]
    return main_diag - pob_diag

def dop(a,rows_len,columns_len): #возвращает алгебраическое дополнение элемента из матрицы
    result=[]
    for i in range(len(a)):
        for j in range(len(a)):
            if i!=rows_len and j!=columns_len: #подбор значений
                result+=[a[i][j]] #запись значения в result
    m2=result[0]*result[3]-result[1]*result[2] #определитель матрицы
    return m2* (-1)**(rows_len+columns_len)

def obr(arr): #возвращает обратную матрицу arr (проверка на истинность)
    if determinant3x3(arr)==0:
        print('Обратной матрицы не существует')
    else:
        f = [[[] for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                q=1/determinant3x3(arr)*dop(arr,i,j)
                if int(q)==q: #int(q)/q
                    f[j][i]=int(q)
                else:
                    f[j][i]=q
        print('Обратная матрица 3*3')
        for rows_len in f:
            print(*rows_len)
obr(a)

# Сравнение времени
import numpy as np
import timeit
print('----------------')
print('Время выполнения нашего кода')

#с помощью timeit сравним скорость
start_time1 = timeit.default_timer()
obr(a)
print(timeit.default_timer() - start_time1)

print('Время выполнения с помощью numpy')
start_time2 = timeit.default_timer()
p = np.linalg.inv(a)
for u in p:
    print(u)
print(timeit.default_timer() - start_time2)