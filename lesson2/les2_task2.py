#  Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется
#  равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.


def sum_recursion(n):
    if n == 1:
        return 1
    return sum_recursion(n - 1) + n


number = int(input('Введите натуральное число: '))

var1 = sum_recursion(number)
var2 = int(number * (number + 1) / 2)

print(f'Сумма чисел от 1 до {number} = {var1}')
print(f'Результат расчета формулы {number}({number}+1)/2 = {var2}')

if var1 == var2:
    print('Числа между собой равны')
else:
    print('Числа не равны')
