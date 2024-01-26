# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без
# использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение —
# частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают или не совпадают в ваших решениях.

string = input('Введите текст: ')
my_set = set(string)
my_dict = {}

# 3 вариант
for i in string:
    my_dict[i] = my_dict.get(i, 0) + 1

# 2 вариант
# for i in my_set:
#     my_dict.setdefault(i, string.count(i))

# 1 вариант
# cnt = 0
# for i in my_set:
#     for j in range(len(string)):
#         if string[j] == i:
#             cnt += 1
#     my_dict[i] = cnt
#     count = 0
print(my_dict)