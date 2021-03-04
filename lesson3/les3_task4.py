# ВВ одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min1, min2 = MAX_ITEM, MAX_ITEM
for num in array:
    if num < min1:
        min1, min2 = num, min1
    elif num < min2:
        min2 = num
print(min1, min2)
