# Изменяемое множество
my_set = {1, 2, 3, 4, 2, 5, 6, 7}
print(my_set)

# Не изменяемое множество
my_f_set = frozenset((1, 2, 3, 4, 2, 5, 6, 7,))
print(my_f_set)

# Ошибка, т.к. помести во множество изменяемый список
# not_set = {1, 2, 3, 4, 2, 5, 6, 7, ['a', 'b']} # TypeError: unhashable type: 'list'

# Метод  add()
my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.add(9)
print(my_set)
my_set.add(7) # Ничего не добавится, т.к. такой элемент уже есть
print(my_set)
# my_set.add(9, 10) # TypeError: сразу 2 элемента добавить нельзя

# Добавили кортеж, воспринимается как один элемент
my_set.add((9, 10))
print(my_set)


# Метод remove() - удаление по значению
my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.remove(5) # удалили 5 элемент
print(my_set)
# my_set.remove(10) # KeyError: 10 нет такого элемента


# Метод discard()
my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.discard(5)
print(my_set)
my_set.discard(10) # При удалении нет ошибки


# Метод intersection() - Получение одинаковых элементов у множеств
my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.intersection(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')

# Аналогичная запись в новой версии Python
my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set & other_set
print(f'{my_set = }\n{other_set = }\n{new_set = }')


# Метод union() - объединение множеств.
my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.union(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')

# Аналогичная запись в новой версии Python
new_set_2 = my_set | other_set
print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')


# Метод difference() - удаляет из левого множества элементы правого.
my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.difference(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')

# Аналогичная запись в новой версии Python
new_set_2 = my_set - other_set
print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')