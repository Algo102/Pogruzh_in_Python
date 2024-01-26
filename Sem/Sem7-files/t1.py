# ✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform

MAX = 1000
MIN = -1000

def write_numbers(file_name: str, count: int):
    with open(file_name, 'w', encoding='utf-8') as file:
        for _ in range(count):
            # file.write(str(randint(MIN, MAX)) + ' | ' + str(uniform(MIN, MAX)))
            file.write(f'{(randint(MIN, MAX))} | {uniform(MIN, MAX)}\n') # можем передавать только строки

write_numbers("nums.txt", 10)