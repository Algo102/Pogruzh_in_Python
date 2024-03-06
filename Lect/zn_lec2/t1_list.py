# Список - упорядоченый набор элементов. В []


# list_1 = []  # создание пустого списка
# list_2 = list()  # создание пустого списка
# # создание заполненного списка
# list_3 = [7, 8, 9, 12, 15]

# print(list_1)
# print(list_3)
# # чтоб при выводе убрать скобки и запятые, ставим *
# print(*list_3)
# print(list_3[0])
# print(list_3[-1]) # ИНДЕКСАЦИЯ С КОНЦА СПИСКА
# print(len(list_3))  # len длина списка или строки

# # Списки работают с циклами
# for i in list_3:
#     print(i)


# list1 = [1, 5]
# list1.append(8) # добавление элемента в конец списка append
# print(list1)

# # Автозаполнение циклом
# list2 = []
# print(list2)
# for i in range(5):
#     list2.append(i)
#     print(i)

# # Заполнение ручным вводом через цикл
# list3 = []
# print(list3)
# for i in range(5):
#     n = int(input())
#     list3.append(n)
# print(list3)

# # Можно добавлять элемент на нужную позицию insert
# list6 = [1, 2, 3, 4]
# print(list6.insert(2, 11)) # None - поэтому можно без print
# print(list6)


# # Удаление последнего елемента pop
# list4 = [12, 6, 5, 4]
# print(list4.pop()) # 4
# print(list4) #[12, 6, 5]
# list4.pop()
# print(list4) # [12, 6]
# a = list4.pop()
# print(a) # выводит и удаляет
# print(list4) # [12]

# # Можно в качестве аргумента указать номер элемента - для удаления его
# list5 = [13, 7, 9, 0]
# print(list5.pop(1))
# print(list5)


# Работа со срезами такая же как и со строками
list7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list7[0])  # 1
print(list7[-1])  # 10
print(list7[len(list7) - 1])  # 10
print(list7[-5])  # 6
print(list7[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list7[:2])  # [1, 2]
print(list7[len(list7) - 2:])  # [9, 10]
print(list7[2:9])  # [3, 4, 5, 6, 7, 8, 9]
print(list7[6:-18])  # []
print(list7[0:len(list7):6])  # [1, 7]
print(list7[::6])  # [1, 7]

# # Изменение нужного элемента
# t = [1, 2, 3, 5]
# print(t)
# t[0] = 2
# print(t)
