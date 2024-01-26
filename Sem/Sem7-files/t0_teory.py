# w - write перезаписывает файл, если нет файла создает
# a - append добавляет, если нет файла создает
# r - read
# r+ = w+ - write and read

# ЗАПИСЫВАЕТ СТРОКУ, список так не примет, цифры нельзя
# file = open('numbers.txt', 'a', encoding='utf-8')
# file.write(input('Введите строку: ') + '\n')
# file.close()

# data = 'Первая строка'
# file = open('numbers.txt', 'w', encoding='utf-8')
# file.write(data) # если в data цифры, то str(data)
# file.close()

# with open('numbers.txt', 'w', encoding='utf-8') as file:
#     file.write(input('Введите строку: ') + '\n')
# print(file)


# ТАК ПРИМЕТ И СПИСОК
data = ['Первая строка', 'ВТОРАЯ', 'Третья']
file = open('numbers.txt', 'w', encoding='utf-8')
file.write('\n'.join(data))
file.close()

