# 📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# 📌 Имена пишите с большой буквы.
# 📌 Каждую пару сохраняйте с новой строки.
import json


def convert_to_json(in_file, out_file):
    data = {}
    with open(in_file, 'r', encoding='utf-8') as f:
        for line in f:
            # strip удаляет пробелы в начале и в конце
            name, number = line.strip().split(' | ')
# новый элемент в словаре data. Ключ - имя, а значение - число
            data[name.strip().capitalize()] = float(number)

    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

convert_to_json('result.txt', 'res.json')