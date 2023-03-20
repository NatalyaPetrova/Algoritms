import math

def str_to_list(s):
    l = s.split()
    for i in range(len(l)):
        l[i] = int(l[i])
    return l

def task_1():
    ms1_str = input('Input m1 and s1: ')
    ms1 = str_to_list(ms1_str)
    ms2_str = input('Input m2 and s2: ')
    ms2 = str_to_list(ms2_str)
    ms3_str = input('Input m3 and s3: ')
    ms3 = str_to_list(ms3_str)
    ms4_str = input('Input m4 and s4: ')
    ms4 = str_to_list(ms4_str)
    n = int(input('Input n: '))
    n_old = n
    n_dict = {}
    coins = {}
    values = [ms1[1], ms2[1], ms3[1], ms4[1]]
    values.sort()
    values.reverse()
    for i in range(len(values)):
        if values[i] == ms1[1]:
            coins[ms1[1]] = ms1[0]
        elif values[i] == ms2[1]:
            coins[ms2[1]] = ms2[0]
        elif values[i] == ms3[1]:
            coins[ms3[1]] = ms3[0]
        elif values[i] == ms4[1]:
            coins[ms4[1]] = ms4[0]
    for i in coins:
        if n == 0:
            break
        k = n // i
        if k <= coins[i]:
            n_dict[i] = k
            n -= i * k
        else:
            n_dict[i] = coins[i]
            n -= i * coins[i]
    s = 0
    for i in n_dict:
        s += i * n_dict[i]
    if s == n_old:
        print(n_dict)
    else:
        print('There is less money, than it needs!')

def task_2():
    exhibits = {'Mona Lisa': '1 10', 'David': '20 15', 'Madonna': '1 7', 'Peacock': '10 20', 'Dance': '3 5', 'Spring': '10 10', 'Eggs': '3 30', '1': '23 99', '2': '3 10',
                '3': '12 50', '4': '3 1', '5': '16 23', '6': '2 5'} #exhibits: weight price
    while True:
        n = int(input(f'Input N (not more than {len(exhibits)}): '))
        if n <= len(exhibits):
            break
        else:
            print('Wrong input!')
    k = int(input('Input K: '))
    m = int(input('Input M: '))
    loot = {}
    #exhibits = {1: 10, 20: 15, 1: 7, 10: 20, 3: 5, 10: 10, 3: 30}
    whole_price = 0
    for i in range(m):
        if n == 0:
            break
        k_new = k
        while True:
            max_price = 0
            exh = ''
            weight = 0
            for j in exhibits:
                price = int(exhibits[j][-2] + exhibits[j][-1])
                if max_price < price and int(exhibits[j][0] + exhibits[j][1]) <= k_new:
                    max_price = price
                    exh = j
                    weight = int(exhibits[j][0] + exhibits[j][1])
            if exh == '':
                break
            if weight < k_new:
                k_new -= weight
                whole_price += max_price
                n -= 1
                exhibits.pop(exh)
                loot[exh] = str(weight) + ' ' + str(max_price)
            else:
                whole_price += max_price
                n -= 1
                exhibits.pop(exh)
                loot[exh] = str(weight) + ' ' + str(max_price)
                break
    print(whole_price)
    print(loot)


def task_3():
    def arg_min(t, s):
        amin = -1
        m = max(t)
        for i in range(len(t)):
            if t[i] < m and i not in s:
                m = t[i]
                amin = i
        return amin

    print('0 - Moscow, 1 - St. Petersburg, 2 - Kazan, 3 - Yekaterinburg, 4 - Novosibirsk, 5 - Vladivostok, 6 - Irkutsk, 7 - Krasnoyarsk, 8 - Omsk, 9 - Nizhny Novgorod, 10 - Kirov')
    cities = [[  0,  635,  815,    0,    0,    0,    0,    0,    0, 410,   0],
              [635,    0, 1208,    0,    0,    0,    0,    0,    0,   0,   0],
              [815, 1208,    0,  892,    0,    0,    0,    0,    0, 419,   0],
              [  0,    0,  892,    0, 1498,    0,    0,    0, 1417,   0,   0],
              [  0,    0,    0, 1498,    0, 6147,    0, 1569,  641,   0,   0],
              [  0,    0,    0,    0, 6147,    0, 4789,    0,    0,   0,   0],
              [  0,    0,    0,    0,    0, 4789,    0, 1060,    0,   0,   0],
              [  0,    0,    0,    0, 1569,    0, 1060,    0, 1422,   0,   0],
              [  0,    0,    0, 1417,  641,    0,    0, 1422,    0,   0,   0],
              [410,    0,  419,    0,    0,    0,    0,    0,    0,   0, 453],
              [  0,    0,    0,    0,    0,    0,    0,    0,    0, 453,   0]]
    n = len(cities)
    t = [math.inf] * n #список с кратчайшими путями
    v = int(input('Input start: '))
    s = [v] #список с просмотренными вершинами
    t[v] = 0
    while v != -1:
        for i in range(len(cities[v])):
            if cities[v][i] > 0:
                if i not in s:
                    t[i] = min(t[i], t[v] + cities[v][i])
        v = arg_min(t, s)
        if v >= 0:
            s.append(v)
    print(t)


'''cities = {
        'Moscow': {'St. Petersburg': 635, 'Kazan': 815, 'Nizhny Novgorod': 410},
        'St. Petersburg': {'Moscow': 635, 'Kazan': 1208},
        'Kazan': {'St. Petersburg': 1208, 'Yekaterinburg': 892, 'Moscow': 815},
        'Yekaterinburg': {'Kazan': 892, 'Novosibirsk': 1498, 'Omsk': 1417},
        'Novosibirsk': {'Yekaterinburg': 1498, 'Vladivostok': 6147, 'Krasnoyarsk': 1569},
        'Vladivostok': {'Novosibirsk': 6147, 'Irkutsk': 4789},
        'Irkutsk': {'Vladivostok': 4789, 'Krasnoyarsk': 1060},
        'Krasnoyarsk': {'Novosibirsk': 1569, 'Irkutsk': 1060, 'Omsk': 1422},
        'Omsk': {'Krasnoyarsk': 1422, 'Yekaterinburg': 1417, 'Novosibirsk': 641},
        'Nizhny Novgorod': {'Moscow': 410, 'Kazan': 419, 'Kirov': 453},
        'Kirov': {'Nizhny Novgorod': 453}
    }
print(cities['Moscow'])
mini = ('', 10000000000)
for i in cities['Moscow']:
    if cities['Moscow'][i] < mini[1]:
        mini = (i, cities['Moscow'][i])
print(mini)'''
while True:
    x = input('Input task number: ')
    if x == '1':
        task_1()
    elif x == '2':
        task_2()
    elif x == '3':
        task_3()
    elif x == '0':
        break
    else:
        print('Wrong input!')