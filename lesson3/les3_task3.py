# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

SIZE = 25
MIN_ITEM = -20
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_negative = MIN_ITEM
idx = 0

for i, num in enumerate(array):
    if num < 0:
        if max_negative < num:
            max_negative = num
            idx = i

print(f'Максимальный отрицательный элемент {max_negative}, его индекс {idx}')
