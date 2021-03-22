# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.

import hashlib

text = input('Введите строку: ')

hash_l = []

for j in range(len(text)):
    for i in range(1, len(text) + 1):
        tmp = (text[j:i])
        tmp_hash = hashlib.md5(tmp.encode('utf-8')).hexdigest()
        if tmp_hash in hash_l or tmp == text or tmp == '':
            continue
        hash_l.append(tmp_hash)

print(len(hash_l))
