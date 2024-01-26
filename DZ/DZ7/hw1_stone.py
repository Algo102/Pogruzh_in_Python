import random
import string
import os


def rand_files(quantity: int):
    f_ext = ['txt', 'jpg', 'mov', 'mp3']
    for _ in range(quantity):
        name = ''.join(random.sample(string.ascii_lowercase, 10)) + '.' + random.choice(f_ext)
        with open(name, 'w', encoding='utf-8') as file:
            file.write(name)

# rand_files(10)

def rename_group(path: str = os.getcwd(), new_name: str = '',
                 count: int = 1, in_ext: str = '',
                 out_ext: str = '___', limits: tuple = (0, 10)):
    counter = 1
    if os.path.isdir(path):
        for file in os.listdir(path):
            split_result = file.rsplit('.', 1)
            if len(split_result) == 2:
                name, ext = split_result
            else:
                # Обработка случая, когда нет точки в имени файла
                name, ext = file, ''
            if ext == in_ext or not in_ext:
                re_name = f'{name[limits[0]:limits[1]]}{new_name if new_name else ""}{counter:0>{count}}.{out_ext}'
                os.rename(os.path.join(path, file), os.path.join(path, re_name))
                count += 1
        return f'Было переименовано {counter - 1}'
    else:
        return 'Это не директория'


rename_group(new_name='NEW', in_ext='mov', out_ext='EXE', count=5, limits=(3, 6))
