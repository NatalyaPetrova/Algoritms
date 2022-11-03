# O(n log n)
testList = [1, 43, 31, 21, 6, 96, 48, 13, 25, 5]


def mergeSort(testList):
    if len(testList) < 2:
        return testList
    middle = int(len(testList) / 2)
    left = mergeSort(testList[:middle])
    right = mergeSort(testList[middle:])
    result = []
    print("Left: ", left)
    print("Right: ", right)
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    result += left
    result += right
    print("Result: ", result)
    return result


print("O(n log n): ")
mergeSort(testList)
print()
