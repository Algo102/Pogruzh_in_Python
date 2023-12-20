# не изменяемый объект - ХЭШи разные
a = 5
print(a, id(a)) # 5 140734072939432
a += 1
print(a, id(a)) # 6 140734072939464

# не даст изменить объект
# txt = 'Hello word'
# txt[5] = '_'

# replace - метод перемещает все заменяя указаные символы
# создавая новый объект
txt = 'Hello word'
print(txt, id(txt))
txt = txt.replace(' ', '_')
print(txt, id(txt))

# переменные ссылаются на один и тот же объект
a = b = 2
print(a, id(a), b, id(b))