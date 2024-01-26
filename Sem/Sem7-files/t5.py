# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.
from t4 import gen_files

# def gen_some_est_files(**kwargs): # бесконечное число переменных
#     for i in kwargs.items():
#         print(i)
#
# gen_some_est_files(exe=5, bmp=3, jpg=23)


def gen_some_est_files(**kwargs):  # бесконечное число переменных
    if kwargs:
        for extension, count in kwargs.items():
            gen_files(extension, count=int(count))


gen_some_est_files(exe=2, bmp=3, jpg=4)