# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
# среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
import random
from random import randint, choice

# val_gl = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
# val_sogl = ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
#
#
# def gen_name():
#     name_len = randint(4, 8)
#     rand_name = ''
#     is_gl = False
#     for i in range(name_len):
#         dict_choice = randint(0, 1)
#         if dict_choice:
#             is_gl = True
#         rand_name += random.choice(val_gl) if dict_choice else random.choice(val_sogl)
#     if not is_gl:
#         rand_name += 'а'
#     return rand_name.capitalize()
#
# def write_names(count: int):
#     with open('names.txt', 'w', encoding='utf-8') as f:
#         for _ in range(count):
#             f.write(gen_name() + '\n')
#
# write_names(5)

# Другое решение
consonant = set([chr(i) for i in range(ord('а'), ord('я') + 1)])
vowels = list('уеаоэяийюё')
consonant = list(consonant.difference(set(vowels)))
first_consonant = list(set(consonant).difference(set(list('ьыъ'))))

MIN_NAME = 4
MAX_NAME = 7


def generate_name(count: int):
    result = []
    for _ in range(count):
        name = choice(first_consonant)
        for i in range(1, randint(MIN_NAME, MAX_NAME)):
            name += choice(vowels) if i % 2 else choice(consonant)
        result.append(name.title())
    with open('names.txt', 'w', encoding='UTF-8') as file:
        file.write('\n'.join(result))


generate_name(10)


