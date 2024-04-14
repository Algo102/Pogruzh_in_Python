# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


import random
from random import randint

# Заполнение списка - 1 вар
# list_1 = []
# n = int(input("Введите количество значений: "))
#
# for i in range(n):
#     m = int(input("Введите значение: "))
#     list_1.append(m)
# print(list_1)


# Заполнение списка - 2 вар
# size = int(input("Enter size of list: "))
# list_1 = []
# for _ in range(size):
#     # list_1.append(random.randint(1, 10))
#     num = random.randint(1,5)
#     list_1.append(num)
#
# print(list_1)


# Заполнение списка - 3 вар (листо комплекеншенс)
size = int(input("Enter size of list: "))
# справа количество циклов, а слева, что помещаем в список каждый цикл
list_1 = [randint(1, 10) for _ in range(size)]
print(list_1)


# Первое решение
print('Различных чисел в списке', len(set(list_1)))


# # Второе решение
list_unique = []
for i in list_1:
    if i not in list_unique:
        list_unique.append(i)

print(len(list_unique))


