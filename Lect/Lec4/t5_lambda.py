# Ананимная функция лямбда
def add_two_def(a, b):
    return a + b

# не принято присваивать переменую, т.к. считается одноразовой
add_two_lambda = lambda a, b: a + b

print(add_two_def(42, 3.14))
print(add_two_lambda(42, 3.14))

my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3, 'ten': 10}
s_key = sorted(my_dict.items()) # Сортировка словаря - ключей
s_value = sorted(my_dict.items(), key=lambda x: x[1]) # Сортировка по значениям с помощью ЛЯМБДЫ
print(f'{s_key = }\n{s_value = }')