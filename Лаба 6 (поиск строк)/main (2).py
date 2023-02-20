import time

def nav_alg(s):
    start = time.time()
    mas = [0] * 100 #создаем масссив для подсчёта чисел
    for j in range(10, 100): #Поиск двузначных чисел
        st = str(j)
        for i in range(len(s) - 1):
            if st[0] == s[i] and st[1] == s[i + 1]:
                mas[j] += 1
    for j in range(len(mas)):
        if mas[j] == max(mas):
            print('Самое часто встречающееся число:', j)
            print('Количество совпадений:', max(mas))
            break
    end = time.time() - start
    print('Время выполнения алгоритма: ', end)
    print('')

def Rabin_Karp(s):
    start = time.time()
    counter = [0] * 100
    alf = 10
    m = 1
    hashmas = [0] * 100
    for i in range(10, 100):
        shablon = i
        hash = (shablon // 10) * alf ** m + (shablon % 10) * alf ** (m - 1)
        hashmas[i] = hash

    for i in range(len(s) - 1):
        ch = int(s[i] + s[i + 1])
        hash = (ch // 10) * alf ** m + (ch % 10) * alf ** (m - 1)
        for j in range(10, len(hashmas)):
            if hashmas[j] == hash:
                if j == ch:
                    counter[ch] += 1

    for j in range(len(counter)):
        if counter[j] == max(counter):
            print('Самое частое число: ', j)
            print('Количество совпадений: ', max(counter))
            break
    end = time.time() - start
    print('Время выполнения алгоритма: ', end)
    print('')

def Boyer_Moore(s):
    start = time.time()
    num_list = [0] * 100
    for i in range(10, 100):
        num = str(i)
        j = 1
        while j < len(s):
            if s[j] == num[1]:
                if s[j - 1] == num[0]:
                    num_list[i] += 1
                    j += 2
                else:
                    j += 2
            else:
                if s[j] == num[0]:
                    j += 1
                else:
                    j += 2
    for j in range(10, len(num_list)):
        if num_list[j] == max(num_list):
            print('Самое частое число: ', j)
            print('Количество совпадений: ', max(num_list))
            break
    end = time.time() - start
    print('Время выполнения алгоритма: ', end)
    print('')

def Knuth_Morris_Pratt(s):
    start = time.time()
    num_list = [0] * 100
    for i in range(10, 100):
        num = str(i)
        if num[0] == num[1]:
            pref_func = [0, 0]
        else:
            pref_func = [0, 1]
        j = 0
        while j < len(s) - 1:
            if num[0] == s[j]:
                if num[1] == s[j + 1]:
                    num_list[i] += 1
                    j += 2
                else:
                    j += 1 - pref_func[1] + 1
            else:
                j += 0 - pref_func[0] + 1
    for j in range(10, len(num_list)):
        if num_list[j] == max(num_list):
            print('Самое частое число: ', j)
            print('Количество совпадений: ', max(num_list))
            break
    end = time.time() - start
    print('Время выполнения алгоритма: ', end)
    print('')

def task_2():
    log = open('1.txt', 'r', encoding="utf8")
    log_list = log.readlines()
    log_str = ''
    for i in range(len(log_list)):
        log_list[i] = log_list[i].replace("\n", "")
        log_str += log_list[i] + ' '
    log_list = []

    log_wiki = open('2.txt', 'r', encoding="utf8")
    log_wiki_list = log_wiki.readlines()
    log_wiki_str = ''
    for i in range(len(log_wiki_list)):
        log_wiki_list[i] = log_wiki_list[i].replace("\n", "")
        log_wiki_str += log_wiki_list[i] + ' '
    log_wiki_list = []

    signs = [' ', '.', ',', '[', ']', '(', ')', '{', '}', '!', '?', '-', '"', '«', '»', ':', ';']

    sh = ''
    for i in range(len(log_str)):
        if signs.count(log_str[i]) == 0:
            sh += log_str[i]
        elif sh != '':
            log_list.append(sh)
            sh = ''

    sh = ''
    for i in range(len(log_wiki_str)):
        if signs.count(log_wiki_str[i]) == 0:
            sh += log_wiki_str[i]
        else:
            log_wiki_list.append(sh)
            sh = ''
    plag = 0
    for i in range(len(log_list) - 2):
        shablon = [log_list[i], log_list[i + 1], log_list[i + 2]]
        j = 2
        k = 0
        while j < len(log_wiki_list):
            if log_wiki_list[j] == shablon[2]:
                if log_wiki_list[j - 1] == shablon[1] and log_wiki_list[j - 2] == shablon[0]:
                    plag += len(shablon[2]) + len(shablon[1]) + len(shablon[0])
                    j += 3
                else:
                    if log_wiki_list[j] == shablon[1]:
                        j += 1
                    elif log_wiki_list[j] == shablon[0]:
                        j += 2
                    else:
                        j += 3
            else:
                if log_wiki_list[j] == shablon[1]:
                    j += 1
                elif log_wiki_list[j] == shablon[0]:
                    j += 2
                else:
                    j += 3
    plag_sum = 0
    for i in range(len(log_wiki_list)):
        plag_sum += len(log_wiki_list[i])
    plag /= plag_sum
    print('Процент плагиата равен ', plag * 100)
    log.close()
    log_wiki.close()

a = [0, 1]
s = '01'
for i in range(2, 500):
    x = a[i - 2] + a[i - 1]
    a.append(x)
    s += str(x)

while True:
    t = input('Введите номер задания: ')
    if t == '1':
        while True:
            print(' 1 - наивный алгоритм\n',
                  '2 - алгоритм Рабина-Карпа\n',
                  '3 - алгоритм Бойера-Мура\n',
                  '4 - алгоритм Кнута-Морриса-Пратта\n',
                  '0 - выход')
            x = input('Введите номер алгоритма: ')
            print('')
            if x == '1':
                nav_alg(s)
            elif x == '2':
                Rabin_Karp(s)
            elif x == '3':
                Boyer_Moore(s)
            elif x == '4':
                Knuth_Morris_Pratt(s)
            elif x == '0':
                exit()
            else:
                print('Некорректный ввод!\n')
    elif t == '2':
        task_2()
    elif t == '0':
        break
    else:
        print('Некорректный ввод!\n')