# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.
my_str = 'hello'
# my_dict = {}
# for item in set(my_str):
#     if item in my_str:
#         my_dict[item] = ord(item)

# my_dict = {key: ord(key) for key in set(my_str) if key in my_str}
my_dict = {key: ord(key) for key in set(my_str)}
print(my_dict)

# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили. Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.

# вывод ключ значение без итератора
# for k, v in my_dict.items():
#     print(k, v)

# вывод ключ значение частично с итератором итератора
# iter_dict = iter(my_dict)
# for i in range(5):
#     key = next(iter_dict, 999)
#     # if key not in my_dict:
#     if key == 999:
#         break
#     else:
#         value = my_dict[key]
#         print("Key:", key, "Value:", value)

# Тот вариант который по заданию
iter_dict = iter(my_dict.items())
for i in range(5):
    print(next(iter_dict, 999))