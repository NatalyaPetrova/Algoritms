file_input = open('sort.in', 'w')
n = int(input('Введите количество '))
for u in range(n):
    file_input.write((input('Введите число ') + ' '))
file_input = open('sort.in', 'r')
arr = list(map(float, file_input.readline().split()))
file_output = open('sort.out', 'w')

# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i,
# что является индексом в arr[]. n - размер кучи


def get_heap(arr, length, index):
    left = 2 * index + 1
    right, max_index = left + 1, index
    # Проверяем существует ли левый дочерний элемент больший, чем корень
    if left < length:
        if arr[max_index] < arr[left]: max_index = left
    # Проверяем существует ли правый дочерний элемент больший, чем корень
    if right < length:
        if arr[max_index] < arr[right]: max_index = right
    # Заменяем корень, если нужно
    if max_index != index:
        arr[max_index], arr[index] = arr[index], arr[max_index]
        get_heap(arr, length, max_index)


# Основная функция для сортировки массива заданного размера
def heap_sort(arr, length):
    # Построение max-heap.
    for i in range(length // 2 - 1, -1, -1):
        get_heap(arr, length, i)
    # Один за другим извлекаем элементы
    for i in range(length - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        get_heap(arr, i, 0)


heap_sort(arr, n)
print(*arr, file=file_output)
print('Cортировка завершена!')
file_output = open('sort.out', 'r')
for w in file_output:
    print(w, end='')
file_output.close()
