# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

def words_list(text):
    len_word = 0;
    words = sorted(text.split())
    for word in words: # ищем самое длинное слово
        if len(word) > len_word:
            len_word = len(word)

    for n, word in enumerate(words, start=1): # бежим по словам и нумеруем их, начиная с 1
        #print(f'{n} {word: >{len_word}}')
        print(n, word.rjust(len_word)) # rjust отступ по правому краю

text = 'hello beautiful word'
words_list(text)