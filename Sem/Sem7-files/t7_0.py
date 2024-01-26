from t6_0 import gen_files

def gen_some_est_files(directory: str, **kwargs):  # бесконечное число переменных
    if kwargs:
        for extension, count in kwargs.items():
            gen_files(directory, extension, count=int(count))


gen_some_est_files('sample', avi=2, mov=3, mkv=4,
                   mp3=4, wav=2, bmp=6, jpg=4, txt=3, doc=5)