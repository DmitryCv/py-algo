# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

MIN_ITEM = 2
MAX_ITEM = 99
count = [0] * 8

for n in range(MIN_ITEM, MAX_ITEM + 1):
    for d in range(2, 10):
        if n % d == 0:
            count[d - 2] += 1
for i, el in enumerate(count):
    print(f'{i + 2} - {el}')
