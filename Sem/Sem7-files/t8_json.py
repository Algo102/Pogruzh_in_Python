import json
# для работы со словарями - ключ-значение

# Запись в файл
# data = {'name': 'Стоун', 'age': 39, 'work': 'GB'}
# with open('example.json', 'w', encoding='utf-8') as file:
#     json.dump(data, file, indent=4, ensure_ascii=False)

# Чтение из файла
with open('example.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print(data)