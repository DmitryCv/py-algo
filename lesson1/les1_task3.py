# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

let1, let2 = input("Введите 2 различные буквы латинского алфавита (без пробелов): ").lower()

let1_pos = ord(let1) - 96
let2_pos = ord(let2) - 96
if let1_pos > let2_pos:
    dif = let1_pos - let2_pos - 1
else:
    dif = let2_pos - let1_pos - 1

print(f'Буква {let1} находится на позиции {let1_pos}\n'
      f'Буква {let2} находится на позиции {let2_pos}\n' 
      f'Количество букв между ними {dif}')
