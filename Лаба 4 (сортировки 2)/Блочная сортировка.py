file_input = open('sort.in', 'w')
n = int(input('Введите количество '))
for u in range(n):
    file_input.write((input('Введите число ') + ' '))
file_input = open('sort.in', 'r')
array = list(map(float, file_input.readline().split()))
file_output = open('sort.out', 'w')


def bucketSort(array):
    largest = max(array)
    length = len(array)
    size = largest / length

    # Create Buckets
    buckets = [[] for i in range(length)]

    # Bucket Sorting
    for i in range(length):
        index = int(array[i] / size)
        if index != length:
            buckets[index].append(array[i])
        else:
            buckets[length - 1].append(array[i])

    # Sorting Individual Buckets
    for i in range(len(array)):
        buckets[i] = sorted(buckets[i])

    # Flattening the Array
    result = []
    for i in range(length):
        result = result + buckets[i]

    return result


result = bucketSort(array)
print(result, file=file_output)
print('Cортировка завершена!')
file_output = open('sort.out', 'r')
for w in file_output:
    print(w, end='')
file_output.close()
