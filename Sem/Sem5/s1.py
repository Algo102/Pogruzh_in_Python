# Пользователь вводит строку из четырёх или более целых чисел,
# разделённых символом “/”. Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа хранятся в кортеже
# как значения второго ключа.

# numbers = input('Введите не менее 4-х чисел, через /: ').split('/')
# print(numbers)
# v1, k1, k2, *v2 = numbers
# my_dict = {int(k1): v1, int(k2): v2}
# print(my_dict)

# другое решение
a, b, c, *d = list(map(int, input('Введите не менее 4-х чисел, через /: ').split('/')))
print(my_dict1 := {b: a, c: d})
