txt = 'Книга называеся "Война и мир".'
print(txt)

# Многострочные строки, без переменной это комментарии
t = """
    savdfvdfdbdb
    zfdfbmlkbmlsmbl
    df;vmxblkmklgb
    """

# конкотинация, не приветствуются, т.к. каждый + это новый объект
# особено нельзя в цикле
LIMIT = 120
ATTENTION = 'Внимание!'
name = input('Твое имя? ')
age = int(input('Твой возраст? '))
text = ATTENTION + 'Хоть тебе и осталось ' + str(100 - age) +\
    " до 100 лет, но длина строки не должна превышать " + str(LIMIT) + ' символов.'
print(text)