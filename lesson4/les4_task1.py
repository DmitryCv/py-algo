# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random
import timeit
import cProfile


def max_negative_wo_sort(size):
    min_item = -100
    max_item = 100
    arr = [random.randint(min_item, max_item) for _ in range(size)]

    max_negative = float('-inf')
    idx = 0

    for i, num in enumerate(arr):
        if num < 0:
            if max_negative < num:
                max_negative = num
                idx = i

    return max_negative, idx


def max_negative_w_sort(size):
    min_item = -100
    max_item = 100
    arr = [random.randint(min_item, max_item) for _ in range(size)]

    max_ = None
    for item in sorted(arr, reverse=True):
        if item < 0:
            max_ = item
            break
    idx = arr.index(max_)
    return max_, idx


def max_negative_w_new_array(size):
    min_item = -100
    max_item = 100
    arr = [random.randint(min_item, max_item) for _ in range(size)]

    neg_array = [num for num in arr if num < 0]
    max_neg = max(neg_array)
    idx = arr.index(max_neg)
    return max_neg, idx


print(timeit.timeit('max_negative_wo_sort(100)', number=100, globals=globals())) # 0.023316300000000012
print(timeit.timeit('max_negative_wo_sort(1000)', number=100, globals=globals())) # 0.19093529999999997
print(timeit.timeit('max_negative_wo_sort(10_000)', number=100, globals=globals())) # 1.8713222
print(timeit.timeit('max_negative_wo_sort(100_000)', number=100, globals=globals())) # 18.804275
print(timeit.timeit('max_negative_wo_sort(200_000)', number=100, globals=globals())) # 38.0137934

cProfile.run('max_negative_wo_sort(100_000)')
'''
Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.282    0.282 <string>:1(<module>)
        1    0.033    0.033    0.270    0.270 les4_task1.py:11(<listcomp>)
        1    0.010    0.010    0.280    0.280 les4_task1.py:8(max_negative_wo_sort)
   100000    0.091    0.000    0.198    0.000 random.py:174(randrange)
   100000    0.039    0.000    0.237    0.000 random.py:218(randint)
   100000    0.073    0.000    0.107    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.282    0.282 {built-in method builtins.exec}
   100000    0.010    0.000    0.010    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   127345    0.024    0.000    0.024    0.000 {method 'getrandbits' of '_random.Random' objects}

'''
print()
print(timeit.timeit('max_negative_w_sort(100)', number=100, globals=globals())) # 0.019301499999997418
print(timeit.timeit('max_negative_w_sort(1000)', number=100, globals=globals())) # 0.19406560000000184
print(timeit.timeit('max_negative_w_sort(10_000)', number=100, globals=globals())) # 1.9890438999999986
print(timeit.timeit('max_negative_w_sort(100_000)', number=100, globals=globals())) # 19.930543099999994
print(timeit.timeit('max_negative_w_sort(200_000)', number=100, globals=globals())) # 40.1401891
cProfile.run('max_negative_w_sort(100_000)')
'''
Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.299    0.299 <string>:1(<module>)
        1    0.002    0.002    0.298    0.298 les4_task1.py:25(max_negative_w_sort)
        1    0.034    0.034    0.275    0.275 les4_task1.py:28(<listcomp>)
   100000    0.092    0.000    0.202    0.000 random.py:174(randrange)
   100000    0.039    0.000    0.241    0.000 random.py:218(randint)
   100000    0.075    0.000    0.110    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.299    0.299 {built-in method builtins.exec}
        1    0.020    0.020    0.020    0.020 {built-in method builtins.sorted}
   100000    0.010    0.000    0.010    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   127252    0.024    0.000    0.024    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

'''
print()
print(timeit.timeit('max_negative_w_new_array(100)', number=100, globals=globals())) # 0.01877489999999682
print(timeit.timeit('max_negative_w_new_array(1000)', number=100, globals=globals())) # 0.18622829999999624
print(timeit.timeit('max_negative_w_new_array(10_000)', number=100, globals=globals())) # 1.8618728999999945
print(timeit.timeit('max_negative_w_new_array(100_000)', number=100, globals=globals())) # 18.645016499999997
print(timeit.timeit('max_negative_w_new_array(200_000)', number=100, globals=globals())) # 37.548311600000005
cProfile.run('max_negative_w_new_array(100_000)')
'''
 Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.278    0.278 <string>:1(<module>)
        1    0.000    0.000    0.276    0.276 les4_task1.py:39(max_negative_w_new_array)
        1    0.035    0.035    0.270    0.270 les4_task1.py:42(<listcomp>)
        1    0.005    0.005    0.005    0.005 les4_task1.py:44(<listcomp>)
   100000    0.090    0.000    0.197    0.000 random.py:174(randrange)
   100000    0.038    0.000    0.235    0.000 random.py:218(randint)
   100000    0.073    0.000    0.107    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.278    0.278 {built-in method builtins.exec}
        1    0.001    0.001    0.001    0.001 {built-in method builtins.max}
   100000    0.010    0.000    0.010    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   127305    0.023    0.000    0.023    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
'''
'''
Выводы: Было проведено сравнение 3-х реализаций поиска максимального отрицательного числа в списке. 
Наиболее медленным оказался алгоритм, который использовал сортировку, а наиболее быстрым - в котором 
использовалось создание дополнительного списка отрицительных элементов, хотя это и потребовало больше
ресурсов памяти.  
'''
