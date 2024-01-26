# f = open('data.txt', 'wb')
# f.write('Привет, '.encode('utf-8') + 'мир!'.encode('cp1251'))
# f.close()
#
# f = open('data.txt', 'r', encoding='utf-8', errors='replace')
# print(list(f))
# f.close()
#
with open('data.txt', 'r+', encoding='utf-8', errors='backslashreplace') as f:
    print(list(f)) # не открывает из-за разной кодировки, добавил errors
#     print(f.write('Пока'))