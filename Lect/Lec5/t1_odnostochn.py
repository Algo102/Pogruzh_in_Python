# Обмен значениями.
# Можно менять любое значение переменных, количество слева = количество справа
a = 42
b = 7
a, b = b, a

# Распаковка и упаковка
# Распаковка.
# Количество введеных, должно соответствовать количеству переменных
a, b, c = input("Введите три символа: ")
print(f'{a=} {b=} {c=}')
a, b, c = {'один', 'два', 'три'}

# В таком случае при не соблюдении соответствия по численности, получим кортеж
t = 1, 2, 3

# Распаковка с упаковкой лишнего-нужного. Чтоб избежать ошибок выше  используют *
data = ["один", "два", "три", "четыре", "пять", ]
a, b, c, *d = data
print(f'{a=} {b=} {c=} {d=}')  # a='один' b='два' c='три' d=['четыре', 'пять']
a, *b, c, d = data
print(f'{a=} {b=} {c=} {d=}')  # a='один' b=['два', 'три'] c='четыре' d='пять'

# Распаковка только нужного, с упаковкой лишнего(не нужного).
# Все лишнее попадает в *_ , а потом не сохраняется
link = 'https://docs.python.org/3/faq/programming.html#how-can-i-pass-optional-or-keyword-parameters-from-one-function-to-another'
prefix, *_, suffix = link.split('/')
print(f'{prefix} {suffix}')

# Вывод всей последовательности без цикла
# Но все ровно идет перебебор и выдача по одному элементу
data = [2, 4, 6, 8, 10, ]
print(*data, sep='\t')

# Множественное присваивание
a = b = c = 0
a += 42
# или
a, b, c = 1, 2, 3

# так нельзя делать с последовательностями, т.к при добавлении элемента
# в один, элемент добавится во все последовательности.
a = b = c = {1, 2, 3}
a.add(42)
print(f'{a=} {b=} {c=}')

# множественное сравнение, подразумеваем что стоит И
a = b = c = 42
# if a == b and b == c:
if a == b == c:
    print('Полное совпадение')

# if a < b and b < c:
if a < b < c:
    print('b больше a и меньше c')

# Задачка
data = {10, 9, 8, 1, 6, 3}
a, b, c, *d, e = data
print(a, b, c, d, e) # 1 3 6 [8, 9] 10
# Т.к. это множество, целые числа хэшируются по возрастанию