# Пользователь вводит число N – общее количество рассматриваемых дней
# (1 ≤ N ≤ 10). Далее построчно N от –50 до 50. Нужно вывести
# наибольшее количество идущих подряд положительных чисел.
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

from random import randint

days = int(input("Введите количество дней "))
count = 0
max_count = 0
for _ in range(days):
    temp = randint(-25, 50)
    print(temp, end=' ')
    if temp > 0:
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 0
# Написали второй раз т.к. не всегда может быть минус последним
# Можно прописать этот ИФ один раз в первом ИФе, но будет программа
# будет работать дольше, если положительных цифр больше
if count > max_count:
    max_count = count
print()
print(max_count)