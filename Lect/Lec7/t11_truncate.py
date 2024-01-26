# truncate(size=None) Если не передать значение то будет удалена часть
# файла от текущей позиции до конца. Возвращает позицию после изменения файла.

# Алгоритм удаления последней строки
# last = before = 0
# with open('new_data.txt', 'r+', encoding='utf-8') as f:
#     while line := f.readline():
#         last, before = f.tell(), last
#     print(f.seek(before, 0))
#     print(f.truncate())

# Если передать параметр size метод изменяет размер файла до указанного числа
# символов или байт от начала файла.

size = 80
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    print(f.truncate(size))

# Если size меньше размера файла, происходит усечение файла. Если size больше
# размера файла, он увеличивается до указанного размера.