# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def sort_ch(text):
    ch_list = []
    for i in set(text):
       ch_list.append(ord(i))
    #print(sorted(ch_list))
    return sorted(ch_list, reverse=True)

#sort_ch('age')
print(sort_ch('age'))
