# Копирование и устройство списков в пайтоне

num = 45  # в переменной число
text = 'hello'  # в переменной текст
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # в переменной ссылка на список-объект
print(my_list)

my_list_2 = my_list  # обе переменные ссылаются на один и тот же список-объект
print(my_list_2)
print()

my_list_2[2] = 999  # поменяв во втором списке элемент
print(my_list)  # [1, 2, 999, 4, 5, 6, 7, 8, 9]
print(my_list_2)  # [1, 2, 999, 4, 5, 6, 7, 8, 9]
# Элемент поменялся и в первом списке, т.к. поменяли элемент по ссылке в одном и том же объекте


# Поэтому СПИСКИ НУЖНО КОПИРОВАТЬ, но копируется только один уровень вложенности, к примеру, список в списке
my_list_3 = my_list.copy()
# my_list_3 = my_list[:]  # аналогичная запись копирования (работают одинакого), но это срез от начала до конца
# my_list_3 = list(my_list)  # третий аналогичный способ копирования
my_list_3[3] = 0

print(my_list)    # [1, 2, 999, 4, 5, 6, 7, 8, 9]
print(my_list_3)  # [1, 2, 999, 0, 5, 6, 7, 8, 9]


list1 = [1, 2, 3, 4, 5, 6, 7, 8, [11, 22, 33, ]]
# list2 = list1.copy()
list2 = list1[:]
print(list1)  # [1, 2, 3, 4, 5, 6, 7, 8, [11, 22, 33]]
print(list2)  # [1, 2, 3, 4, 5, 6, 7, 8, [11, 22, 33]]

# поменяв в последнем элементе второй элемент у второго списка, он поменялся и у первого спика,
# т.к.вложенный список не скопировался, а остался ссылкой на объект
list2[-1][1] = '~~~'
print(list1)  # [1, 2, 3, 4, 5, 6, 7, 8, [11, '~~~', 33]]
print(list2)  # [1, 2, 3, 4, 5, 6, 7, 8, [11, '~~~', 33]]


# ЧТОБ КОПИРОВАТЬ ВСЕ УРОВНИ НУЖНО ИСПОЛЬЗОВАТЬ БИБЛИОТЕКУ copy, т.е. создаются разные объекты
from copy import deepcopy
list3 = [1, 2, 3, 4, [55, 66, [777, 888]]]
list4 = deepcopy(list3)

list3[-1][-1][-1] = 'XXX'
print(list3)  # [1, 2, 3, 4, [55, 66, [777, 'XXX']]]
print(list4)  # [1, 2, 3, 4, [55, 66, [777, 888]]]

# Все то же самое касается картежей, т.к. кортеж отличается от списков только тем,
# что его нельзя менять, но если в нем есть в ложенные списки, то все условия,
# как для списков сохраняются.

# По сути такая запись не имеет смысл, т.к. кортежи не изменны
my_tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
my_tuple2 = my_tuple1

# Изменив список у первого кортежа изменится и у второго
my_tuple1 = (1, 2, 3, 4, [5, 6, 7, 8, 9])
my_tuple2 = my_tuple1


# Нет смысла так копировать, т.к. copy копирует только первый уровень, а это
# кортеж, в втором уровне список, но это ссылка на объект
my_tuple1 = (1, 2, 3, 4, [5, 6, 7, 8, 9])
my_tuple2 = my_tuple1[:]  # копирование через срез от начала до конца
# my_tuple2 = my_tuple1.copy()  # функциональность полностью идентичная

# А вот таким образом, при копировании создается новый объект
my_tuple3 = deepcopy(my_tuple1)