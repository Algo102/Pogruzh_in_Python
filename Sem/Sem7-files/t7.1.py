import os
import shutil

group_ext = {
    'video': ['mov', 'avi', 'mkv'],
    'audio': ['mp3', 'wav'],
    'image': ['bmp', 'jpg']
}

def sort_dir(directory: str):
    for file in os.listdir(directory):
        # print(file)
        ext = file.split('.')[-1]
        for file_group, ext_group in group_ext.items():
            if ext in ext_group:
                if not os.path.exists(os.path.join(directory, file_group)):
                    os.mkdir(os.path.join(directory, file_group))
                shutil.move(os.path.join(directory, file), os.path.join(directory, file_group, file))

sort_dir('sample')