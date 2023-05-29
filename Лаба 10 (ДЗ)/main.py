import random

def task_1():
    def row_data(k):
        if data[k][0] == data[k][1] == data[k][2]:
            s = str(data[k][0]) + ' win'
            return s
        return 0
    def col_data(k):
        if data[0][k] == data[1][k] == data[2][k]:
            s = str(data[0][k]) + ' win'
            return s
        return 0
    def diag_data():
        if data[0][0] == data[1][1] == data[2][2] or data[0][2] == data[1][1] == data[2][0]:
            s = str(data[1][1]) + ' win'
            return s
        return 0

    data = [[], [], []]
    flag = 0
    s_data = input('Input data: ')
    for i in range(len(s_data)):
        data[i // 3].append(int(s_data[i]))
        if i == 2 or i == 5 or i == 8:
            print(data[i // 3])
    for i in range(3):
        if row_data(i) != 0:
            print(row_data(i))
            flag = 1
            break
        elif col_data(i) != 0:
            print(col_data(i))
            flag = 1
            break
    if flag == 0:
        if diag_data() == 0:
            print('Draw')
        else:
            print(diag_data())

def task_2():
    matrix = [[1, 3, 10, 12],
    [10, 11, 16, 20],
    [23, 30, 34, 50]]
    print(matrix)
    target = int(input('Input target: '))

    rows = len(matrix)
    cols = len(matrix[0])
    row = 0
    col = cols - 1
    flag = 0
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            print(row, col)
            flag = 1
            break
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    if flag == 0:
        print('Wrong target! ')

def task_3():
    n = 8
    board = [[0] * n for _ in range(n)]

    solutions = []

    def is_safe(row, col):
        for i in range(row):
            if board[i][col] == 1:
                return False
            if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
                return False
            if col + (row - i) < n and board[i][col + (row - i)] == 1:
                return False
        return True

    def place_queen(row):
        if row == n:
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append('Q')
                    else:
                        solution.append('.')
            solutions.append(solution)
        else:
            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = 1
                    place_queen(row + 1)
                    board[row][col] = 0

    place_queen(0)
    print(len(solutions))


def task_4(n):
    if n == 0 or n == 1: 
        return 1
    elif n == 2:  
        return 2
    else:
        ways = [0] * (n + 1)
        ways[0] = 1
        ways[1] = 1
        ways[2] = 2
        
        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2] + ways[i - 3]

        return ways[n]

def task_5():
    class ThreeStacks:
      def __init__(self, array_size):
          self.array_size = array_size
          self.stack_array = [None] * array_size
          self.top1 = -1  # Вершина стека 1
          self.top2 = array_size // 3 - 1  # Вершина стека 2
          self.top3 = 2 * (array_size // 3) - 1  # Вершина стека 3

      def push(self, stack_number, value):
          if stack_number == 1:
              if self.top1 < self.array_size // 3 - 1:
                  self.top1 += 1
                  self.stack_array[self.top1] = value
              else:
                  print("Стек 1 переполнен.")
          elif stack_number == 2:
              if self.top2 < 2 * (self.array_size // 3) - 1:
                  self.top2 += 1
                  self.stack_array[self.top2] = value
              else:
                  print("Стек 2 переполнен.")
          elif stack_number == 3:
              if self.top3 < self.array_size - 1:
                  self.top3 += 1
                  self.stack_array[self.top3] = value
              else:
                  print("Стек 3 переполнен.")
          else:
              print("Неверный номер стека.")

      def pop(self, stack_number):
          if stack_number == 1:
              if self.top1 >= 0:
                  value = self.stack_array[self.top1]
                  self.stack_array[self.top1] = None
                  self.top1 -= 1
                  return value
              else:
                  print("Стек 1 пуст.")
                  return None
          elif stack_number == 2:
              if self.top2 >= self.array_size // 3:
                  value = self.stack_array[self.top2]
                  self.stack_array[self.top2] = None
                  self.top2 -= 1
                  return value
              else:
                  print("Стек 2 пуст.")
                  return None
          elif stack_number == 3:
              if self.top3 >= 2 * (self.array_size // 3):
                  value = self.stack_array[self.top3]
                  self.stack_array[self.top3] = None
                  self.top3 -= 1
                  return value
              else:
                  print("Стек 3 пуст.")
                  return None
          else:
              print("Неверный номер стека.")
              return None
    '''Для реализации трех стеков с использованием одномерного массива можно применить подход, 
       называемый "фиксированное разделение".
       Идея заключается в том, чтобы разделить одномерный массив на три равные части и выделить 
       каждую часть для одного стека. Таким образом, каждый стек будет иметь свою область в массиве.
       Необходимо определить размер массива и начальные индексы для каждого стека. Предположим, что у нас 
       есть массив stack_array определенного размера array_size. 
       В этом примере класс ThreeStacks содержит методы push и pop, которые позволяют добавлять элементы в 
       соответствующий стек и извлекать элементы из стека соответственно. Индексы вершин каждого стека (top1, top2, top3) 
       обновляются при добавлении и удалении элементов. Если стек переполняется или пуст, выводится соответствующее сообщение.
       Обратите внимание, что в этом примере стеки имеют фиксированный размер, который определяется размером массива. 
       Если требуется изменяемый размер стеков, то следует использовать динамическую структуру данных, такую как связанный список.'''

def task_6():
    def exponential_filter(input_value, output_value, alpha):
        output_value = alpha * input_value + (1 - alpha) * output_value
        return output_value

    input_value = float(input('Input_value: '))
    output_value = float(input('Output_value: '))
    alpha = float(input('Alpha: '))
    if 0 < alpha < 1:
        print(exponential_filter(input_value, output_value, alpha))
    else:
        print('Wrong alpha!')

def task_7():
    data = []
    flag = 0
    for i in range(random.randint(0, 100)):
        data.append(random.randint(0, 50))
    print(data)
    marked = [False] * (len(data) + 1)
    for num in data:
        if 0 <= num <= len(data):
            marked[num] = True
    for i in range(1, len(data) + 1):
        if not marked[i]:
            print('Наименьшее пропущенное число:', i)
            flag = 1
            break
    if flag == 0:
        print('Наименьшее пропущенное число:', len(data) + 1)


while True:
    x = input('Input the task: ')
    if x == '1':
        task_1()
    elif x == '2':
        task_2()
    elif x == '3':
        task_3()
    elif x == '4':
      n = int(input('Введите длину лестницы: '))
      result = task_4(n)
      print(f"Количество возможных вариантов перемещения по лестнице из {n} ступенек: {result}")
    elif x == '5':
        task_5()
    elif x == '6':
        task_6()
    elif x == '7':
        task_7()
    elif x == '0':
        break
    else:
        print('Wrong input!')
