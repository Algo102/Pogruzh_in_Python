import random as rnd
from sys import builtin_module_names as bmn, path as p
# Ч.з., перечисляются объекты модуля, но не сами модули
# Если загрузили объект ч.з. псевдоним, то обращаемся к нему только ч.з. псевдоним
# Если загрузили объект ч.з. from, то обращаться к модулю не получиться, т.к. его не загрузили

print(bmn)
print(*p, sep='\n')
print(rnd.randint(1, 6))
# print(path) # NameError: name 'path' is not defined
# print(sys.path) # NameError: name 'sys' is not defined
# print(sys.p)

# При использовании такой переменной, не возникнет проблем с доступами к приватным и защищенным переменным
# А также нормально подгрузятся константы и функции, в противном случае их можно перезаписать
__all__ = ['func', '_secret']  # но нужно не забывать держать список актуальным
SIZE = 100 # Константы
_secret = 'qwerty' # защищенная переменная
__top_secret = '1q2w3e4r5t6y' # приватная переменная
def func(a: int, b: int) -> str:
    z = f'В диапазоне от {a} до {b} получили {rnd.randint(a, b)}'
    return z
result = func(1, 6)