# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга,
# а значение — кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться
# на любое большее количество друзей.

frds_stuff = {
    'fr1': ('палатка', 'топор', 'еда', 'пиво'),
    'fr2': ('палатка', 'вилка', 'вода', 'пиво'),
    'fr3': ('палатка', 'топор', 'вода', 'пиво'),
    'fr4': ('палатка', 'топор', 'вода', 'лимонад'),
} # Коллекция друзей
set1 = set()
for k in frds_stuff:
    if not set1:
        set1 = set(frds_stuff[k])
    else:
        set1 &= set (frds_stuff[k])
print('Вещь есть у всез друзей: ', set1)

my_tuple = frds_stuff.keys()
my_set = []
for frnd in my_tuple:
    my_set = set(frds_stuff[frnd])

    for other_frnds in [i for i in my_tuple if i != frnd]:
        my_set = my_set - set(frds_stuff[other_frnds])
    if my_set:
        print(f'Уникальная вещь у  {frnd}:', *my_set)

for frnd in my_tuple:
    my_set = []
    to_remove = set(frds_stuff[other_frnds])
    for other_frnds in [i for i in my_tuple if i != frnd]:
        if not my_set:
            my_set = set(frds_stuff[other_frnds])
        else:
            my_set = my_set & set(frds_stuff[other_frnds])
    my_set -= to_remove

    if my_set:
        print(f'У всех есть {my_set}, кроме {frnd}')