# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def digit_sum(number: str) -> int:
    total = 0
    for n in number:
        total += int(n)
    return total


num = int(input('Введиты количество чисел: '))
max_sum = 0

for _ in range(num):
    num_cur = input('Введите число: ')
    num_sum = digit_sum(num_cur)
    if max_sum < num_sum:
        max_sum, max_num = num_sum, num_cur

print(f'Наибольшее число по сумме цифр {max_num} и сумма его цифр {max_sum}')
