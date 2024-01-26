# Читаем через метод readline
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline():
        print(res) # выводит через строку, т.к. в конце каждой строки и у принта свои переносы

# Вывод по строчно, но не более 100 символов
SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline(SIZE):
        print(res)

with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
        print(line[:-1])
        print(line.replace('\n', ''))