from collections import defaultdict

ent_num = int(input('Введите число предприятий: '))
if ent_num < 2:
    print('Должно быть как минимум 2 предприятия.')
    exit(0)
ent = defaultdict(list)
ent_profit = defaultdict(list)

for n in range(1, ent_num + 1):
    name = input(str(n) + '-е предприятие: ')
    profit = list(map(int, input('Прибыль за 4 квартала (4 числа через пробел): ').split(' ')))
    ent[name] = sum(profit) / len(profit)
avg = sum(ent.values()) / len(ent)

for n, p in ent.items():
    if p > avg:
        ent_profit['Прибыль выше среднего'].append(n)
    elif p < avg:
        ent_profit['Прибыль ниже среднего'].append(n)

for key, value in ent_profit.items():
    print(f'{key} {value}')
