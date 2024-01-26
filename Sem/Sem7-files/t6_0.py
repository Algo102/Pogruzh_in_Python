from random import randint, randbytes, choice
from string import ascii_lowercase
import os


MIN_NAME = 3
MAX_NAME = 4
MIN_SIZE = 256
MAX_SIZE = 4096
COUNT = 42
def gen_files(directory: str, ext: str, min_name : int = MIN_NAME, max_name : int = MAX_NAME,
                 min_size: int = MIN_SIZE, max_size: int = MAX_SIZE, count: int = COUNT):
    count = count if 0 < count <= COUNT else randint(1, COUNT)
    for _ in range(count):

        cur_min_name = min_name if (MIN_NAME <= min_name < MAX_NAME) else MIN_NAME
        cur_max_name = max_name if (MIN_NAME < max_name <= MAX_NAME) else MAX_NAME
        cur_min_size = min_size if (MIN_SIZE <= min_size < MAX_SIZE) else MIN_SIZE
        cur_max_size = max_size if (MIN_SIZE < max_size <= MAX_SIZE) else MAX_SIZE

        name = ''
        for _ in range(min([cur_min_name, cur_max_name]), max([cur_min_name, cur_max_name]) + 1):
            name += choice(list(ascii_lowercase))
        if not os.path.exists(directory):
            os.mkdir(directory)
        if name in list(map(lambda x: x.split('.')[0], os.listdir(directory))):
            name += '_1'
        file_name = os.path.join(directory, name + '.' + ext[:3])
        with open(file_name, 'wb') as file:
            file.write(randbytes(randint(cur_min_size, cur_max_size)))


if __name__ == '__main__':
    gen_files('sample', 'exe', min_name=3, max_name=3, count=4)
