# 📌 Напишите функцию, которая преобразует pickle файл хранящий
# список словарей в табличный csv файл.
# 📌 Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# 📌 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
import csv
import pickle

# создаем свой pickle
# data = [
#     {'name': 'Stone', 'age': 38, 'work': 'GB'},
#     {'name': 'Гриша', 'age': 28, 'work': 'Дома'},
#     {'name': 'Алекс', 'age': 18, 'work': 'Работа'}
# ]
#
# with open('sample.pickle', 'wb') as file_pickle:
#     pickle.dump(data, file_pickle)

def pickle_to_csv(path: str):
    result = []
    with open(path, 'rb') as pickle_file:
        dict_data = pickle.load(pickle_file)
    # print(dict_data)
    headers = [header for header in dict_data[0]]
    # print(headers)
    for header in headers:
        row = []
        for contact in dict_data:
            row.append(contact[header])
        result.append(row)
    # print(result)
    with open(path.split('.')[0] + '.csv', 'w', encoding='utf-8') as csv_file:
        cs_wr = csv.writer(csv_file, dialect='excel', delimiter='|', lineterminator='\n')
        cs_wr.writerow(headers)
        cs_wr.writerows(list(zip(*result)))


pickle_to_csv('sample.pickle')
# pickle_to_csv('res.pickle')
# pickle_to_csv('workers.pickle')
# pickle_to_csv('workers_new.pickle')
