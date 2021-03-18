# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
import random

MIN_ITEM = -100
MAX_ITEM = 100
SIZE = 10

array = [random.randint(MIN_ITEM, MAX_ITEM - 1) for _ in range(SIZE)]
print(array)

changes = True
n = len(array)
for _ in range(n - 1):
    changes = False
    for i in range(n - 1):
        if array[i] < array[i + 1]:
            changes = True
            array[i], array[i + 1] = array[i + 1], array[i]
    if not changes:
        break
print(array)
