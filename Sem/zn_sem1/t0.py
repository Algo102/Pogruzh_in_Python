# hi = "Привет"
# n = input(f'{hi}, введи число: ')  # Можно f строкой
# print(int(float(n)))  # Чтоб не было ошибки при вводе дробного числа

name = 'John'
age = 25
print('Привет, меня зовут %s' % name)
print('Привет, меня зовут {} мне {} лет'.format(name, age))
print('Привет, меня зовут {a} мне {b} лет'.format(a=name, b=age))
print(f'Привет, меня зовут {name} мне {age = } лет')


# a = 'phython !'
# print(*a)
# print(*a, sep='\n')

# b = 'Привет, меня зовут Вася'
# z = 'Hello word'
# age = '25'
# age_2 = 40

# print(a, b, z)
# print(a, end=' ')
# print(b, end=' ')
# print(z)
#
# print(b, end='~~~!!!!~~~')
# print(a, end=z)
# print(z)

# print(a, b, z, sep=" ", end='\n')  # sep and аргументы по умолчанию
# print(a, b, z, sep="***")
# print(a, b, z, sep=age)
# print(a, b, z, sep=f'{age_2}')
# print(a, b, z, sep=str(age_2))
# print(a, b, z, sep="\t")
# print(a, b, z, sep="\n")

