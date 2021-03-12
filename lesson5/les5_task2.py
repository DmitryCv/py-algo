from collections import defaultdict, deque


dhex = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11,
        'c': 12, 'd': 13, 'e': 14, 'f': 15}

num1 = deque(input('Введите положительное шестнадцатиричное число: ').lower())
num2 = deque(input('Введите положительное шестнадцатиричное число: ').lower())

k, diff = 0, 0
res = deque()

if len(num1) < len(num2):
    num1, num2 = num2, num1
diff = len(num1) - len(num2)
if diff != 0:
    for _ in range(diff):
        num2.appendleft('0')
num1.reverse()

for n1 in num1:
    n2 = num2.pop()
    res.appendleft((dhex[n1] + dhex[n2] + k) % 16)
    k = 1 if dhex[n1] + dhex[n2] > 15 else 0
if k == 1:
    res.appendleft(1)

for d in res:
    print(list(dhex.keys())[list(dhex.values()).index(d)], end='')
