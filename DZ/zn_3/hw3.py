# В настольной игре Скрабл (Scrabble) каждая буква имеет
# определенную ценность. В случае с английским алфавитом очки
# распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного
# пользователем слова. Будем считать, что на вход подается только
# одно слово, которое содержит либо только английские, либо только
# русские буквы.
# Ввод: ноутбук
# Вывод: 12






dict_1 = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1, 'a': 1, 'e': 1, 'i': 1,
          'o': 1, 'u': 1, 'l': 1, 'n': 1, 's': 1, 't': 1, 'r': 1, 'D': 2, 'G': 2, 'd': 2, 'g': 2, 'B': 3, 'C': 3,
          'M': 3, 'P': 3, 'b': 3, 'c': 3, 'm': 3, 'p': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'f': 4, 'h': 4,
          'v': 4, 'w': 4, 'y': 4, 'K': 5, 'k': 5, 'J': 8, 'X': 8, 'j': 8, 'x': 8, 'Q': 10, 'Z': 10, 'q': 10, 'z': 10}
dict_2 = {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1, 'а': 1, 'в': 1, 'е': 1, 'и': 1,
          'н': 1, 'о': 1, 'р': 1, 'с': 1, 'т': 1, 'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2, 'д': 2, 'к': 2,
          'л': 2, 'м': 2, 'п': 2, 'у': 2, 'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3, 'б': 3, 'г': 3, 'ё': 3, 'ь': 3,
          'я': 3, 'Й': 4, 'Ы': 4, 'й': 4, 'ы': 4, 'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5, 'ж': 5, 'з': 5, 'х': 5,
          'ц': 5, 'ч': 5, 'Ш': 8, 'Э': 8, 'Ю': 8, 'ш': 8, 'э': 8, 'ю': 8, 'Ф': 10, 'Щ': 10, 'Ъ': 10, 'ф': 10, 'щ': 10,
          'ъ': 10}

word = input('Введите слово: ')
# print(word)
list_1 = list()

count = 0
for i in range(len(word)):
    elem = word[i]
    list_1.append(elem)

    for item in dict_1:
        if elem == item:
            for j in dict_1:
                if list_1[i] == j:
                    # print(dict_1[j])
                    count += dict_1[j]
    for item in dict_2:
        if elem == item:
            for j in dict_2:
                if list_1[i] == j:
                    # print(dict_2[j])
                    count += dict_2[j]

# print(list_1)
print(count)

# count = 0
# for i in range(len(word)):
#     elem = input("Повторите слово побуквенно: ")
#     list_1.append(elem)

#     for j in dict_1:
#         if list_1[i] == j:
#           print(dict_1[j])
#           count += dict_1[j]

# print(list_1)
# print(count)


# # ДРУГОЕ РЕШЕНИЕ
# dict_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JZ', 10: 'QZ'}
# dict_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word2 = input().upper()  # перевод букв в верхний регистр
# count2 = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in dict_en:
#             if i in dict_en[j]:
#                 count2 = count2 + j
#     else:
#         for j in dict_ru:
#             if i in dict_ru[j]:
#                 count2 = count2 + j
#
# print(count2)
