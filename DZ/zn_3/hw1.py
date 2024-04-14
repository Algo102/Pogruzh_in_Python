# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. В последующих строках
# записаны N целых чисел Ai.
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

from random import randint


quntity = int(input("Enter array size: "))
min1 = int(input("Enter minimum number: "))
max1 = int(input("Enter maximum number: "))
find = int(input("Enter the number you are looking for: "))

list1 = [randint(min1, max1) for i in range(quntity)]
print(list1)
count = list1.count(find)

print(f'The number {find} appears {count} times.')


# list_1 = []
# numbers = int(input("Введите количество значений: "))
#
# for i in range(numbers):
#     elem = int(input("Введите значение: "))
#     list_1.append(elem)
# print(list_1)
#
# find = int(input("Введите искомое значение: "))
#
# count = 0
# for i in list_1:
#     if find == i:
#         count += 1
# print("Ваше число встречается ", count, " раз")
#
# # Или так
# for i in range(len(list_1)):
#     if find == list_1[i]:
#         count +=1
#
# # А можно воспользоваться функцией count
# print(list_1.count(find))
