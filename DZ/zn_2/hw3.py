# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8
# 17 -> 1 2 4 8 16

n = int(input("Введите число до которого рассчитать 2 в степени "))
if n == 1:
    print(1)
if n == 2:
    print(2)
for i in range(int(n/2)):
    if 2 ** i <= n:
        print(2 ** i, end=' ')

# Другое решение
i = 0
while 2 ** i <= n:
    print(2**i)
    i += 1
