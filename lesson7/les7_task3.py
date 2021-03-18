# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random
# Set size here
ARRAY_SIZE = 2

MIN_ITEM = 0
MAX_ITEM = 20
SIZE = 2 * ARRAY_SIZE + 1

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def find_median(arr, left, right):

    part_index = left
    j = left
    while j < right:
        if arr[j] < arr[right]:
            arr[part_index], arr[j] = arr[j], arr[part_index]
            part_index += 1
        j += 1

    arr[part_index], arr[right] = arr[right], arr[part_index]
    if left <= right:
        mid = len(arr) // 2

        if part_index == mid:
            return arr[part_index]

        if part_index >= mid:
            return find_median(arr, left, part_index - 1)
        else:
            return find_median(arr, part_index + 1, right)

    return


print(f'Медиана = {find_median(array, 0, len(array) - 1)}')
