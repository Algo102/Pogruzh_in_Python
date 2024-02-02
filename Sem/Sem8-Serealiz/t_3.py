# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.
import json
import csv


def json_to_csv(j_file: str):
    with open(j_file, 'r', encoding='utf-8') as json_file:
        js_dict = json.load(json_file)

    user_list = []
    for us_lvl, user in js_dict.items():
        for us_id, us_name in user.items():
            user_list.append((us_name, us_id, us_lvl))

    # print(user_list)
    # чтоб не было пропусков строки можно newline = '' в open вместо lineterminator='\n'
    with open(j_file.split('.')[0] + '.csv', 'w', encoding='utf-8') as csv_file:
        cs_write = csv.writer(csv_file, dialect='excel', delimiter='|', lineterminator='\n')
        cs_write.writerow(['Имя', 'ID', 'Leve'])
        for row in user_list:
            cs_write.writerow(row)

json_to_csv('workers.json')