# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

MIN_ITEM = 0
MAX_ITEM = 50
SIZE = 10

array = [random.uniform(MIN_ITEM, MAX_ITEM - 1) for _ in range(SIZE)]
print(array)


def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2
        left, right = arr[:mid], arr[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        if i < len(left):
            arr[k:] = left[i:]
        if j < len(right):
            arr[k:] = right[j:]

    return arr


print(merge_sort(array))
