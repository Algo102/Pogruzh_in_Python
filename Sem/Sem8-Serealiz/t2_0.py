# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json


def inp_us_data():
    user_data = {}
    while True:
        name = input('Введите имя или exit для выхода: ')
        if name.lower() == 'exit':
            break
        id_number = input('Ведите свой идентификатор: ')

        while True:
            access_level_str = input('Введите уровень доступа от 1 до 7: ')
            if access_level_str.isdigit():
                access_level = int(access_level_str)
                if 1 <= access_level <= 7:
                    break
            print('Вводите от 1 до 7')
        user_data[id_number] = {
            'name': name,
            'access_level': access_level
        }
        save_us_data(user_data, access_level)


def save_us_data(user_data, access_level):
    filename = f'users_access_level_{access_level}.json'
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    # обновляем
    data.update(user_data)

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    inp_us_data()

# нет проверки уникальности идентификатора