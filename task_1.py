# version 1
def min_max(arr):
    if len(arr) == 1:
        return (arr[0], arr[0])
    elif len(arr) == 2:
        # return (min(arr), max(arr))
        if arr[0] < arr[1]:
            return (arr[0], arr[1])
        return (arr[1], arr[0])

    half = len(arr) // 2
    left_min, left_max = min_max(arr[:half])
    right_min, right_max = min_max(arr[half:])

    # return (min(left_min, right_min), max(left_max, right_max))

    # or
    if left_min < right_min:
        fin_min = left_min
    else:
        fin_min = right_min
    if left_max > right_max:
        fin_max = left_max
    else:
        fin_max = right_max
    return (fin_min, fin_max)


array = [1, 3, 5, 6, 7, 9, 24, 56, 67, 45, 34, 32, 57, 0, -2, 56]

print(min_max(array))


# version 2, no sub arrays with slicing, just indicies,  better complexity
def min_max_1(arr, left, right):
    if left == right:
        return (arr[left], arr[left])

    elif right == left + 1:
        if arr[left] < arr[right]:
            return (arr[left], arr[right])
        return (arr[right], arr[left])

    mid = (left + right) // 2
    left_min, left_max = min_max_1(arr, left, mid)
    right_min, right_max = min_max_1(arr, mid + 1, right)

    if left_min < right_min:
        fin_min = left_min
    else:
        fin_min = right_min
    if left_max > right_max:
        fin_max = left_max
    else:
        fin_max = right_max
    return (fin_min, fin_max)


array = [
    1,
    3,
    5,
    6,
    7,
    9,
    24,
    56,
    67,
    45,
    34,
    32,
    57,
    0,
    -2,
    56,
    109,
    -23,
    34,
    45,
    56,
    67,
]

result = min_max_1(array, 0, len(array) - 1)
print(result)
