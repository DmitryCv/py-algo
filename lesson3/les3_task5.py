# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE_N = 4
SIZE_M = 6
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M)] for _ in range(SIZE_N)]
print(*matrix, sep='\n')

max_in_min = MIN_ITEM

for i in range(SIZE_M):
    min_in_col = matrix[0][i]
    for row in matrix:
        if min_in_col > row[i]:
            min_in_col = row[i]
    if max_in_min < min_in_col:
        max_in_min = min_in_col
print(max_in_min)
