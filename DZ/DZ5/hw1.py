# Напишите функцию get_file_info, которая принимает на вход
# строку - абсолютный путь до файла. Функция возвращает кортеж из
# трёх элементов: путь, имя файла, расширение файла.
# На входе: file_path = "C:/Users/User/Documents/example.txt"
# На выходе: ('C:/Users/User/Documents/', 'example', '.txt')

file_path = 'file_path = "C:/Users/User/Documents/example.txt"'

def get_file_info(file_path):
    f_name_full = file_path.split("/")[-1]
    f_xxx ='.' + f_name_full.split('.')[-1]
    f_name = f_name_full[:-len(f_xxx)]
    path = file_path[:-len(f_name_full)]
    return (path, f_name, f_xxx)

print(get_file_info(file_path))

# def get_file_info(file_path):
#     file_name = file_path.split("/")[-1]
#     file_extension = file_name.split(".")[-1]
#     path = file_path[:-len(file_name)]
#     return (path, file_name[:-len(file_extension)-1], "." + file_extension)