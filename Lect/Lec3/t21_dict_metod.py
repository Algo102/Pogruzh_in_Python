# Метод setdefault - похож не get, но отсутствующий ключ добавляется в словарь.
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}

# В словаре нет, возвращает и добавляет None
spam = my_dict.setdefault('five')
print(f'{spam = }\t{my_dict=}')

# В словаре нет, возвращает и добавляет default
eggs = my_dict.setdefault('six', 6)
print(f'{eggs = }\t{my_dict=}')

# В словаре есть, возвращает значение
new_spam = my_dict.setdefault('two')
print(f'{new_spam=}\t{my_dict=}')

# В словаре есть, возвращает значение, default не учитывает
new_eggs = my_dict.setdefault('one', 1_000)
print(f'{new_eggs=}\t{my_dict=}')


# Метод keys возвращает объект-итератор dict_keys.
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.keys()) # dict_keys(['one', 'two', 'three', 'four', 'ten'])

# for для перебора ключей словаря
for key in my_dict.keys():
    print(key)

# отработает аналогично, т.к если нет метода, то идет итерация по ключам
for key in my_dict:
    print(key)


# Метод values похож на keys, но возвращает значения в виде объекта итератора
print(my_dict.values())
for value in my_dict.values():
    print(value)


# Метод items используют в цикле, когда необходимо работать одновременно
# с ключами и значениями, как с парами.
print(my_dict.items())

for tuple in my_dict.items(): # плохо
    print(tuple)
    print(f'{tuple[0] = } value before 100 - {100 - tuple[1]}')

for key, value in my_dict.items(): # хорошо
    print(f'{key = } value before 100 - {100 - value}')


# Метод popitem для удаления последней пары ключ значение из словаря.
# Если измените значение у существующего ключа, положение
# ключа в очереди не меняется, он не считается последним добавленным
# удаление происходит справа налево, по методу LIFO.
spam = my_dict.popitem()
print(f'{spam = }\t{my_dict=}')

eggs = my_dict.popitem()
print(f'{eggs = }\t{my_dict=}')


# Метод pop удаляет пару ключ-значение по переданному ключу.
spam = my_dict.pop('two')
print(f'{spam = }\t{my_dict=}')
# err = my_dict.pop('six') # KeyError: 'six'
# err = my_dict.pop() # TypeError: нужен аргумент


# Метод update для расширения словаря новыми значениями.
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10, }
my_dict.update(dict(six=6)) # В конец добавили пару six: 6
print(my_dict)

my_dict.update(dict([('five', 5), ('two', 42)])) # добавили five и обновили two
print(my_dict)


# Объединение нескольких словарей в новый
# При одинаковых ключах в словарях, значение берется м последнего(правого)
new_dict = my_dict | {'five': 5, 'two': 42} | dict(six=6)
print(new_dict)

# Практика
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.setdefault('ten', 555))
print(my_dict.values())
print(my_dict.pop('one'))
my_dict['one'] = my_dict['four']
print(my_dict)