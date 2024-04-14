# Создали не пустой словарь
# В словаре может быть и вложенность и другие словари и списки и ...
# Для словаря, ключи это своеобразная индексация
# Ключ изменить нельзя, только через удаление

# slovar = {'1': 'one', '2': 'two', 'two': 'two'}
# print(slovar)
#
# # Добавление в словарь
# slovar['pr'] = 'hello'
# print(slovar)

# # # Пробегаемся и выводим ключи
# for item in slovar:
#     print(item)
#
# # # Выводим ключи и значение
# for item in slovar:
#     print(item, slovar[item])
#
# # # Или так правильнее
# for (key, value) in slovar.items():
#     print(key, value)  # Тут можно указать либо ключ или значение
#
# # Для примера, вывел все пары, у кого значение two
# for (key, value) in slovar.items():
#     if value == 'two':
#         print(key, value)

# # Меняем значение работая в цикле
# for (key, value) in slovar.items():
#     if key == '1':
#         slovar[key] = "111"
# print(slovar)

# Удаление ключа
# del slovar['1']

# Т.к. через цикл удалить не получится, т.к. изменится размерность словаря
# то удалять в цикле можно через список. Удалил все пары со значением two
# lst = []
# for key, value in slovar.items():
#     if value == 'two':
#         lst.append(key)
# for element in lst:
#     del slovar[element]
# print(slovar)


# # Записываем словарь в список списков
# lst = []
# for key, value in slovar.items():
#     lst.append([key, value])
# print(lst)


# # Срезы у списков
spisok = [1, 2, 3, 4, 5, 6, 7]
spisok2 = spisok[:2] + spisok[6:]  # первые 2(до второго индекса) + после 6-го
print(spisok2)  # [1, 2, 7]

spisok3 = spisok[::2]  # третий параметр это шаг
print(spisok3)  # [1, 3, 5, 7]

spisok4 = spisok[::-1]  # третий параметр это шаг, он может идти справа налево
print(spisok4)  # [7, 6, 5, 4, 3, 2, 1]
