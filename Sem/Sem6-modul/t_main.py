# Улучшаем задачу 2.
# 📌 Добавьте возможность запуска функции “угадайки” из модуля в командной
# строке терминала.
# 📌 Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# 📌 Для преобразования строковых аргументов командной строки в числовые
# параметры используйте генераторное выражение.


from t2_rand import serch_num, params
from t4_test import test, puzzle_sol, puz_count_print
from t6_calendar import data_check



print(serch_num(*params[:3]))

print(test('Зимой и летом', ['Ель', 'Елка', 'Сосна'], 3))

print(puzzle_sol(5))
puz_count_print()

print(data_check('22.11.2000'))


