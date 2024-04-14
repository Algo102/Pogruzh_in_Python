# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9] k = 3
# Output: [7, 8, 9, 1, 2, 3, 4, 5, 6]

n = int(input('Введите количество целых чисел: '))
numbers = [i for i in range(1, n+1)]
print(numbers)
k = int(input('Введите какой сдвиг: '))
print(numbers[-k:] + numbers[:-k])
#
# # Другое решение
# for _ in range(k):
#     last_num = numbers.pop()  # удаляет и возвращает последне число
#     numbers.insert(0, last_num)  # Вставляем в нужную позицию в отличае от append - в конец
# # т.е. берем последний элемент и вставляем в начало 3 числа
# print(numbers)



# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# k = int(input("Введите смещение: "))
# list_2 = list_1.copy()+list_1.copy()
# list_3 = []
#
# for i in range(len(list_1)):
#     list_3.insert(i, list_2[i+(len(list_1)-k)])
# print(list_3)
#

# # Второе решение
# print(list_2[len(list_1)-k:(len(list_1)-k)+len(list_1):1])
#

# # Третье решение
# print(list_1[len(list_1)-k:] + list_1[:len(list_1)-k:1])
# # То же самое
# print(list_1[-k:] + list_1[:-k:1])

