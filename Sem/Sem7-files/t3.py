# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

# with open('names.txt', 'r', encoding='utf-8') as file:
    # print(file.read()) # Считывает все строки вертикально визуально, но по факту 'Хушй\nВйщеы\nНябаъак\nКйчё'
    # print(file.read().__repr__()) # 'Хушй\nВйщеы\nНябаъак\nКйчё'
    # print(file.readline()) # Хушй - использовать в цикле, т.к. каждый вызов считывает следующую строку
    # print(file.readlines()) # ['Хушй\n', 'Вйщеы\n', 'Нябаъак\n', 'Кйчё']
    # print([row.strip() for row in file.readlines()]) # ['Хушй', 'Вйщеы', 'Нябаъак', 'Кйчё']
    # print(file.read().split('\n')) # ['Хушй', 'Вйщеы', 'Нябаъак', 'Кйчё']
    # print(list(map(lambda x: x.strip(), file.readlines()))) # ['Хушй', 'Вйщеы', 'Нябаъак', 'Кйчё']

    # file.seek(34) # можно установить курсор на 34 символа, для начала считывания


with open('names.txt', 'r', encoding='utf-8') as f_names:
    names = [row.strip() for row in f_names.readlines()]

with open('nums.txt', 'r', encoding='utf-8') as f_nums:
    nums = [row.strip() for row in f_nums.readlines()]

numbers = []
for row in nums:
    first, second = row.split(' | ')
    numbers.append((int(first), float(second)))

res = []
max_len = len(max([names, numbers], key=len))
for i in range(max_len):
    number = numbers[i%len(numbers)][0] * numbers[i%len(numbers)][1]
    res.append((names[i%len(names)].upper(), round(number)) if number > 0 else (names[i%len(names)].lower(), abs(number)))


with open('result.txt', 'w', encoding='utf-8') as res_file:
    res_file.write('\n'.join([f'{row[0]} | {row[1]}' for row in res]))

# for row in res:
#     print(row)
