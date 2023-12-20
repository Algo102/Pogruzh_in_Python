# Срезы
text = 'Hello world!'
print(text[6]) # w
print(text[3:7]) # lo w, можно и применять шаг

# Метод replace()
# Так как строка не изменяемая, то для замены нужно создать новую
new_txt = text.replace('l', 'L', 2)
# l - что ищем, L - на что меняем, 2 - количество замен (можно не указывать)
print(text, new_txt, sep='\n')


text = 'Hello world!'
print(text.count('l')) # 3 Количество вхождений
print(text.index('l')) # 2 Первое вхождение, при отсутствии ошибка
print(text.find('l')) # 2 Первое вхождение
print(text.find('z')) # -1 При отсутствии -1

print(text[::-1]) # !dlrow olleH - реверс

# Метод split() - разбиение строки на элементы
link = 'https://habr.com/ru/users/dzhoker1/posts/'
urls = link.split('/') # вместо / можно использовать хоть сколько символов
print(urls)

# Разбили ввод пользователя
a, b, c = input('Введите 3 числа через пробел: ').split()
print(c, b, a)

# Если боимся что пользователь введет больше чисел
# Все лишнее сохранится во временную переменную *_
a, b, c, *_ = input('Введите 3 числа через пробел: ').split()
print(c, b, a)


# Метод join() - собирает строки из элементов
data = ['https:', '', 'habr.com', 'ru', 'users', 'dzhoker1', 'posts', '']
url = '/'.join(data) # вместо / можно использовать хоть сколько символов
print(url)


# Методы upper, lower, title, capitalize
text = 'однажды в СТУДЁНУЮ зИмнЮЮ ПоРУ. и тоГда'
print(text.upper()) # ОДНАЖДЫ В СТУДЁНУЮ ЗИМНЮЮ ПОРУ
print(text.lower()) # однажды в студёную зимнюю пору
print(text.title()) # Однажды В Студёную Зимнюю Пору
print(text.capitalize()) # Однажды в студёную зимнюю пору


# Методы startswith и endswith
# Имеет старт и стоп
text = 'Однажды в студёную зимнюю пору'
print(text.startswith('Однажды')) # Совпадает ли начало True
print(text.endswith('зимнюю', 0, -5)) # Совпадает ли конец True, тут конец за минусом 5 символов

text = 'Привет, мир!'
print(text.find(' ')) # 7
print(text.title()) # Привет, Мир!
print(text.split()) # ['Привет,', 'мир!']
print(f'{text = :>25}') # text =              Привет, мир!