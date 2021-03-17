import math
import timeit
import cProfile


def sieve(n):
    if n == 1: return 2
    # k-ое простое не превосходит 1,5 k ln( k ) при k > 1:
    n_range = int(1.5 * n * math.log(n)) + 1
    a = [i for i in range(n_range + 1)]

    a[1] = 0
    b = []
    m = 2
    while m <= n_range:
        if a[m] != 0:
            b.append(a[m])
            for j in range(m, n_range + 1, m):
                a[j] = 0
        m += 1
    return b[n - 1]


def prime(n):
    b = [2]
    n_range = int(1.5 * n * math.log(n)) + 1

    for i in range(2, n_range + 1):
        for j in b:
            if i % j == 0:
                break
        else:
            b.append(i)
    return b[n - 1]


print(timeit.timeit('sieve(10_000)', number=1, globals=globals()))  # 0.0654277
print(timeit.timeit('prime(10_000)', number=1, globals=globals()))  # 7.1577512
cProfile.run('sieve(10_000)')
cProfile.run('prime(10_000)')

'''
         12859 function calls in 0.071 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.071    0.071 <string>:1(<module>)
        1    0.060    0.060    0.070    0.070 les4_task2.py:6(sieve)
        1    0.009    0.009    0.009    0.009 les4_task2.py:9(<listcomp>)
        1    0.000    0.000    0.071    0.071 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method math.log}
    12853    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         12859 function calls in 7.064 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    7.064    7.064 <string>:1(<module>)
        1    7.050    7.050    7.061    7.061 les4_task2.py:23(prime)
        1    0.009    0.009    0.009    0.009 les4_task2.py:26(<listcomp>)
        1    0.000    0.000    7.064    7.064 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method math.log}
    12853    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''
'''
В результате проведенного сравнения алгоритмов "решето Эратосфена" и простого перебора всех чисел 
в списке, выяснилось, что при N = 10_000 разница в скорости составила 110 раз в пользу первого.
'''