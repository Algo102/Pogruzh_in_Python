pwd = 'text'
res = input('Input password: ')
if res == pwd:
    print("Доступ разрешен")
    my_math = int(input('2 + 2 = '))
    if 2 + 2 == my_math:
        print('All ok')
    else:
        print("Не верно")
else:
    print("Пароль не верный")
print("Работа завершена")