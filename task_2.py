# Quick select
import random


def partitioning(arr, left, right, pivotIndex):
    pivotValue = arr[pivotIndex]
    arr[pivotIndex], arr[right] = arr[right], arr[pivotIndex]

    storeIndex = left
    for i in range(left, right):
        if arr[i] < pivotValue:
            arr[storeIndex], arr[i] = arr[i], arr[storeIndex]
            storeIndex += 1

    arr[right], arr[storeIndex] = arr[storeIndex], arr[right]
    return storeIndex


def find_el(arr, left, right, k):
    if left == right:
        return arr[left]

    # picking median of three for pivot index in order for better performance
    mid = (left + right) // 2
    pivot_candidates = [(arr[left], left), (arr[mid], mid), (arr[right], right)]
    pivot_candidates.sort()
    pivotIndex = pivot_candidates[1][1]

    # alternative, simpler
    # pivotIndex = random.randint(left, right)

    pivotIndex = partitioning(arr, left, right, pivotIndex)

    if k == pivotIndex:
        return arr[k]
    elif k < pivotIndex:
        return find_el(arr, left, pivotIndex - 1, k)
    else:
        return find_el(arr, pivotIndex + 1, right, k)


array = [7, 10, 4, 3, 20, 15]
result = find_el(array, 0, len(array) - 1, 0)
print(result)
