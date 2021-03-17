import random
import sys


def get_size(obj, seen=None):
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__iter__') and not isinstance(obj, str):
        size += sum([get_size(i, seen) for i in obj])
    return size


def max_negative_wo_sort(arr):
    max_negative = float('-inf')
    idx = 0

    for i, num in enumerate(arr):
        if num < 0:
            if max_negative < num:
                max_negative = num
                idx = i
    return locals()


def max_negative_w_sort(arr):
    max_ = None
    for item in sorted(arr, reverse=True):
        if item < 0:
            max_ = item
            break
    idx = arr.index(max_)
    return locals()


def max_negative_w_new_array(arr):
    neg_array = [num for num in arr if num < 0]
    max_neg = max(neg_array)
    idx = arr.index(max_neg)
    return locals()


megabyte = 1024 * 1024
MIN_ITEM = -100
MAX_ITEM = 100
SIZE = 500_000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'max_negative_wo_sort использует {get_size(max_negative_wo_sort(array)) / megabyte:.2f} Mb ')
print(f'max_negative_wo_sort использует {get_size(max_negative_w_new_array(array)) / megabyte:.2f} Mb ')
print(f'max_negative_wo_sort использует {get_size(max_negative_w_sort(array)) / megabyte:.2f} Mb ')
'''
Результат работы программы:
max_negative_wo_sort использует 10.42 Mb 
max_negative_wo_sort использует 12.44 Mb 
max_negative_wo_sort использует 10.42 Mb 
Как и ожидалось, вариант функции в которой использовался дополнительный массив для сохранения результата,
занимает больше пространства в памяти. 


Python 3.7.7 [Microsoft Windows 10 64 bit v.1900 (AMD64)] on win32
'''
