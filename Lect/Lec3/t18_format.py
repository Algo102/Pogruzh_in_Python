name = 'Alex'
age = 12
text1 = 'Меня зовут %s и мне %d лет' % (name, age)
print(text1)

text2 = 'Меня зовут {} и мне {} лет'.format(name, age)
print(text2)

text3 = f'Меня зовут {name} и мне {age} лет'
print(text3)

print(f'{{Фигурные скобки}} и {{name}}') # уже как текст

pi = 3.1415
print(f'Число Пи с точностью два знака: {pi:.2f}') # 2 знака после, и float

data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
for item in data:
    print(f'{item:>10}') # > выравнивание справа, < слева, ^ по центру. 10 символов в ячкейке

num = 2 * pi * data[1]
print(f'{num = :_}') # 27_420_988_204.556 авто разделение по 3