import json

my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование", "путешествия"],
    "age": 35,
    "children": [
        {
            "first_name": "Алиса",
            "age": 5
        },
        {
            "first_name": "Маруся",
            "age": 3
        }
    ]
}

# # Записали в файл, но т.к. не указали кодировку русские буквы в ascii
# print(f'{type(my_dict) = }\n{my_dict = }')
# with open('new_user.json', 'w') as f: # {"first_name": "\u0414\u0436\u043e\u043d",
#     json.dump(my_dict, f)
#
# # Открываем его с кодировкой и все ОК
# with open('new_user.json', 'r', encoding='utf-8') as f:
#     new_dict = json.load(f)
# print(f'{new_dict = }')

# # В таком виде можно писать что все значении верны, и кирилица принисается нормально
# with open('new_user.json', 'w', encoding='utf-8') as f:
#     json.dump(my_dict, f, ensure_ascii=False)

# Сохраняем в виде строки
dict_to_json_text = json.dumps(my_dict)
print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')

# Сохраняем в виде строки с учетом кириллицы
dict_to_json_text = json.dumps(my_dict, ensure_ascii=False)
print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')