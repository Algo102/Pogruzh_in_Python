import os
import logging
from collections import namedtuple

logging.basicConfig(filename='info.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s', encoding='utf-8')

FileInfo = namedtuple(
    'FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def get_dir_info(path_f):
    try:
        files_stat = []

        for i in os.listdir(path_f):
            path_full = os.path.join(path_f, i)

            if os.path.isdir(path_full):
                name, extension = os.path.splitext(i)
                files_stat.append(
                    FileInfo(name=name, extension='',
                             is_directory=True, parent_directory=path_f))
            else:
                name, extension = os.path.splitext(i)
                files_stat.append(
                    FileInfo(name=name, extension=extension, is_directory=False,
                             parent_directory=path_f))

        return files_stat
    except Exception as e:
        logging.error(f'Нет информации о файле: {e}',
                      exc_info=True)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print('Запуск: python direct_info.py <path>')
        sys.exit(1)

    dir_path = sys.argv[1]

    files = get_dir_info(dir_path)

    if files:
        for file in files:
            logging.info(f'\n   Имя файла: {file.name}'
                         f'\n   Расширение файла: {file.extension}'
                         f'\n   Директория?: {file.is_directory}'
                         f'\n   Родительская директория: {file.parent_directory}')
    else:
        logging.warning('Файлы отсутствуют')
