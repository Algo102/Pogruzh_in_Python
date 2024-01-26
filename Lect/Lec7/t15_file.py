import os
from pathlib import Path
import shutil

# # Переименовать файл ч.з. os
# os.rename('old1.txt', 'new1.txt')
#
# # Переименовать файл ч.з. Path
# p = Path('old2.txt')
# p.rename('new2.txt')
#
# # Переименовать файл ч.з. Path другой вариант
# Path('old3.txt').rename('new3.txt')


# Перенос файлов с возможностью переименования
# os.replace('new1.txt', os.path.join(os.getcwd(), 'dir', 'new_name.py'))
#
# old_file = Path('new2.txt')
# new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file)


# Копирование с возможностью переименования
# shutil.copy('new3.txt', 'dir')
# shutil.copy2('data.txt', 'dir')
# shutil.copy2('txt.txt', 'dir/txt_new.txt')

# Копирование папки со всем содержимым
# shutil.copytree('dir', 'one_more_dir')

# Удаление папки со всем содержимым
# shutil.rmtree('dir')

# Удаление конкретного файла
os.remove('one_more_dir/data.txt')
Path('one_more_dir/new_name.py').unlink()