# 📌 Создайте модуль с функцией внутри.
# 📌 Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
# 📌 Программа возвращает номер попытки, с которой была
# отгадана загадка или ноль, если попытки исчерпаны.
# ----------------------------
# 📌 Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# 📌 Ключ словаря - загадка, значение - список с отгадками.
# 📌 Функция в цикле вызывает загадывающую функцию, чтобы
# передать ей все свои загадки.
# ----------------------------
# 📌 Добавьте в модуль с загадками функцию, которая принимает на вход строку
# (текст загадки) и число (номер попытки, с которой она угадана).
# 📌 Функция формирует словарь с информацией о результатах отгадывания.
# 📌 Для хранения используйте защищённый словарь уровня модуля.
# 📌 Отдельно напишите функцию, которая выводит результаты угадывания из
# защищённого словаря в удобном для чтения виде.
# 📌 Для формирования результатов используйте генераторное выражение.

from random import randint, choice

__all__ = ['test', 'puzzle_sol', 'puz_count_print']


def test(text: str, variant: list[str], tries: int) -> int:
    print(text)
    variant_v = list(map(lambda x: x.lower(), variant))
    num = 0
    while num < tries:
        user_inp = input('Введите вариант ответа: ').lower()
        num += 1
        if user_inp in variant_v:
            return num
        else:
            print('Вы не угадали')
    return 0


def puzzle_sol(count: 2):
    dict_puz = {
        'Зимой и летом': ['Елка', 'Ель', 'Елочка'],
        'Висит груша': ['Лампочка', 'Лама'],
        'Не лает не кусает': ['Замок', 'Дверь', 'Засов'],
    }
    count = count if count < len(dict_puz) else len(dict_puz)

    for _ in range(count):
        cur_puzzle = choice(list(dict_puz))
        cur_value = dict_puz.pop(cur_puzzle)
        result = test(cur_puzzle, cur_value, randint(1, 3))
        puzz_count(cur_puzzle, result)


_dict_prot = {}


def puzz_count(text: str, trie: int):
    _dict_prot[text] = trie


def puz_count_print():
    for puz_text, puz_count in _dict_prot.items():
        print(f'Загадку {puz_text}' + (f' угадали с {puz_count} попытки' if puz_count else 'не угадали'))


if __name__ == '__main__':
    print(puzzle_sol(5))
    puz_count_print()
