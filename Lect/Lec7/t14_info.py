import os
from pathlib import Path

# # Вывод ввиде списка
# print(os.listdir())
#
# # Вывод по строчно
# p = Path(Path().cwd())
# for obj in p.iterdir():
#     print(obj)


# Проверяем, это папка, файл или ссылка. Ч.з. os получаем строки
# dir_list = os.listdir()
# for obj in dir_list:
#     print(f'{os.path.isdir(obj) = }', end='\t')
#     print(f'{os.path.isfile(obj) = }', end='\t')
#     print(f'{os.path.islink(obj) = }', end='\t')
#     print(f'{obj = }')


# Проверяем, это папка, файл или ссылка. Ч.з. Path получаем объект
# p = Path(Path().cwd())
# for obj in p.iterdir():
#     print(f'{obj.is_dir() = }', end='\t')
#     print(f'{obj.is_file() = }', end='\t')
#     print(f'{obj.is_symlink() = }', end='\t')
#     print(f'{obj = }')


# Обход папок ч.з. walk
for dir_path, dir_name, file_name in os.walk(os.getcwd()):
    print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')