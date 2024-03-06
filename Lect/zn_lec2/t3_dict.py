# Словари, неупорядоченные объекты с доступом по ключу
# Два варианта создания пустого словаря
d = {}
d = dict()

# Для внесения данных используем ключ
d['q'] = 'qwerty'
# print(d)

d['w'] = '123456'
# print(d)

d['p'] = 34
# print(d)  # Вывод всего словаря

# print(d['q'])  # Вывод конкретных данных по ключу

# del d['p']  # Удаление элемента из словаря по ключу
# print(d)

print(d.items())

for item in d:
    print(item)  # Вывод ключей

# for item in d:
#     print('{} : {}'.format(item, d[item]))
#
# for item in d:
#     print(f'{item} : {d[item]}')
#
# for (k, v) in d.items():
#     print('{} : {}'.format(k, v))