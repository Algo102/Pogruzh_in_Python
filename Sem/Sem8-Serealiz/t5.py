# Напишите функцию, которая ищет json файлы в указанной директории
# и сохраняет их содержимое в виде одноимённых pickle файлов.
from t_2 import load_json
import os
import json
import pickle


def save_pickle(filename, data):
    with open(filename, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)


def searc_json(dir_name: str):
    for obj in os.listdir(os.path.join(os.getcwd(), dir_name)):
        filename, file_ext = obj.split('.')
        if file_ext == 'json':
            json_dict = load_json(obj)
            save_pickle(filename+'.pickle', json_dict)

searc_json('test')