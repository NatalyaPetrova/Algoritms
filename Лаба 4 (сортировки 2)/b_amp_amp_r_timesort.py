import random
import timeit


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)


# ---------------------------------------------------
def comb_sort(nums):
    shrink_fact = 1.3
    gaps = len(nums)
    swapped = True
    i = 0

    while gaps > 1 or swapped:
        gaps = int(float(gaps) / shrink_fact)

        swapped = False
        i = 0

        while gaps + i < len(nums):
            if nums[i] > nums[i + gaps]:
                nums[i], nums[i + gaps] = nums[i + gaps], nums[i]
                swapped = True
            i += 1
    return nums


# ---------------------------------------------------
alf = 'абвгдежзийклмнопрстуфхцчшщъыьэюabcdefghijklmnopqrstuvwxyАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮABCDEFGHIJKLMNOPQRSTUVWXY ,.:/\|-+=_'


def main():
    print('---------------------------------------------------\n'
          'Выберете сортировку:\n'
          '1) Быстрая сортировка\n'
          '2) Сортировка расческой\n')
    ans = input('Введите номер действия: ')
    if ans != '':
        file_input = open('sort.in', 'w')
        n = int(input('Введите количество '))
        for u in range(n):
            file_input.write((input('Введите число ') + ' '))
        file_input = open('sort.in', 'r')
        nums = list(map(float, file_input.readline().split()))
        file_output = open('sort.out', 'w')
        for k in ans:
            if k in alf:
                print('Ошибка! Неправильный ввод.')
                main()
                break
        if int(ans) == 1:
            start_time = timeit.default_timer()
            quicksort(nums)
            end_time = timeit.default_timer() - start_time
            print(*nums, file=file_output)
            print('Cортировка завершена!')
            file_output = open('sort.out', 'r')
            for w in file_output:
                print(w, end='')
            file_output.close()
            print('Время выполнения quicksort')
            print(end_time)
        elif int(ans) == 2:
            start_time = timeit.default_timer()
            comb_sort(nums)
            end_time = timeit.default_timer() - start_time
            print(*nums, file=file_output)
            print('Cортировка завершена!')
            file_output = open('sort.out', 'r')
            for w in file_output:
                print(w, end='')
            file_output.close()
            print('Время выполнения comb_sort')
            print(end_time)
        else:
            print('Ошибка! Неправильный ввод.')
            main()
    else:
        print('Ошибка! Неправильный ввод.')
        main()


main()
