# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2

from random import randint

number_of_coins = int(input("Введите количество монет на столе: "))
count_0 = 0
count_1 = 0
for i in range(number_of_coins):
    # coin = int(input(f"Положение монеты {i + 1} (0 или 1): "))
    coin = randint(0, 1)
    print(coin, end=' ')
    if coin == 0:
        count_0 += 1
    else:
        count_1 += 1
print()
if count_0 < count_1:
    print(count_0)
else:
    print(count_1)

