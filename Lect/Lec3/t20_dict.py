# Три способа создания словаря
a = {'one': 42, 'two': 3.14, 'ten': 'Hello world!'}
b = dict(one=42, two=3.14, ten='Hello world!')
c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello world!')])
print(a == b == c)

# Добавление элемента в словарь
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
x = 10
my_dict['ten'] = x
print(my_dict)

# Доступ к значению по ключу через []
TEN = 'ten'
print(my_dict['two'])
print(my_dict[TEN])
# print(my_dict[1]) # такого ключа нет

# Доступ к значению через метод get()
print(my_dict.get('two'))
print(my_dict.get('five'))
print(my_dict.get('five', 5))
print(my_dict.get('ten', 5))