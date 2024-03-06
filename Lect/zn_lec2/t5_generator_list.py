# Работа с генератором списка

# Создаем список от 1 до 100
# list_1 = []
# for i in range(1, 101):
#     list_1.append(i)
# print(list_1)

# Гораздо проще через генератор
# list_2 = [i for i in range(1, 101)]
# print(list_2)


# Добавляем условие (только четные числа)
list_3 = [i for i in range(2, 101) if i % 2 == 0]
print(list_3)

# Или создаем пары каждому из чисел (КОРТЕЖИ)
list_4 = [(i, i) for i in range(2, 101) if i % 2 == 0]
print(list_4)

# Или каждое число мы можем умножать, делить, прибавлять, вычитать
list_5 = [i * 2 for i in range(2, 10) if i % 2 == 0]
print(list_5)