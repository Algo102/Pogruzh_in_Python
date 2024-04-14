# Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint
max_r = 40
lst = [randint(1, max_r) for i in range(15)]
cur_num = int(input("Enter your number: "))
print(lst)
delta = max_r
for i in range(len(lst)):
    mod = abs(lst[i] - cur_num)
    if mod < delta:
        delta = mod
        find_num = lst[i]

print(f'The nearest number is {find_num}')








# list_1 = []
# numbers = int(input("Введите количество значений: "))
#
# for i in range(numbers):
#     elem = int(input("Введите значение: "))
#     list_1.append(elem)
# print(list_1)
#
# find = int(input("Введите ваше число: "))
#
# # Ищем разности между введеным числом
# set_1 = list()
# for i in range(numbers):
#     if list_1[i] > find:
#         set_1.append(list_1[i] - find)
#     else:
#         set_1.append(find - list_1[i])
# # print(set_1)
#
# # Находим минимальную разницу и ее позицию
# min = set_1[0]
# pos = 0
# for i in range(numbers):
#     if min > set_1[i]:
#         min = set_1[i]
#         pos = i
#
# print("Ближайшая цифра к вашему числу: ",
#       list_1[pos])
# print(
#     f"Она находится на позиции {pos+1} и разница с вашим числом, составляет {min}")
#
# # Другое решение
# m = abs(find - list_1[0]) # модуль числа
# min2 = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - find):
#         m = abs(list_1[i] - find)
#         min2 = list_1[i]
# print(min2)