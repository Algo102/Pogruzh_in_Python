import os
from pathlib import Path
import shutil

# Смотрим текущие пути
# print(os.getcwd())
# print(Path.cwd())

# Вышли на 2 папки вверх
# os.chdir('../..')
# print(os.getcwd())
# print(Path.cwd())

# Создали 2 папки
# os.mkdir('new_os_dir')
# Path('new_path_dir').mkdir()

# Создание цепочки каталогов, при условии что промежуточные папки тоже отсутствуют
# os.makedirs('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').mkdir(parents=True)

# удаление папок. Удаляется только самая глубокая папка, т.к. у нее нт содержимого
# os.rmdir('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').rmdir()

# удаление каталога со всем его содержимым
# shutil.rmtree('dir/other_dir')
# shutil.rmtree('some_dir')

# указание пути, в данном случае до файла
file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
print(f'{file_1 = }\n{file_1}')
file_2 = Path().cwd() / 'dir' / 'new_file.txt'
print(f'{file_2 = }\n{file_2}')