# открытие
f = open('text.txt', 'r', encoding='utf-8')
print(f)
print(list(f))

# дозапись
f = open('text.txt', 'a', encoding='utf-8')
f.write('Окончание файла\n')
f.close()

# открытие
f = open('text.txt', 'r', encoding='utf-8')
# print(f)
print(list(f))


# open(file, mode='r', buffering=-1, encoding=None,
# errors=None, newline=None, closefd=True, opener=None)
#
# ✔ 'r' — открыть для чтения (по умолчанию)
# ✔ 'w' — открыть для записи, предварительно очистив файл
# ✔ 'x' — открыть для эксклюзивного создания. Вернёт ошибку, если файл уже существует
# ✔ 'a' — открыть для записи в конец файла, если он существует
# ✔ 'b' — двоичный режим
# ✔ 't' — текстовый режим (по умолчанию)
# ✔ '+' — открыты для обновления (чтение и запись)
