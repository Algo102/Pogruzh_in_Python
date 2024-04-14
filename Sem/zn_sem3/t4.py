# Дан массив, состоящий из целых чисел. Напишите программу,
# которая подсчитает количество элементов массива, больших
# предыдущего (элемента с предидущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

from random import randint

size = int(input('Enter a size array: '))

# list2 = []
# for _ in range(size):
#     num = randint(-5, 5)
#     list2.append(num)

# то же самое с помощью лист комплекейшн
list2 = [randint(-5, 5) for _ in range(size)]
print(list2)

count2 = 0
for i in range(len(list2) - 1):
    if list2[i+1] > list2[i]:
        count2 += 1
        print(f'The number is {list2[i+1]} > {list2[i]}')
print(count2)


# то же самое с помощью лист комплекейшн
# Список заполняется единицами при выполнении условия вместо count
list2 = [1 for i in range(len(list2) - 1) if list2[i+1] > list2[i]]
print(list2)

# Чтоб вывести результат одной цифрой либо len() либо sum()
# Если вместо 1 указать другую цифру или букву то len не прокатит
print(len(list2))
print(sum(list2))



# list1 = [0, -1, 5, 2, 3]
#
# count = 0
# for i in range(len(list1)-1):
#     if list1[i+1] > list1[i]:
#         count += 1
#         print(f'{list1[i + 1]} > {list1[i]}')
# print(count)


# # Или так
# count = 0
# for i in range(1, len(spis)):
#     if spis[i-1] < spis[i]:
#         count += 1
#         print(spis[i], " > ", spis[i-1])
# print(count)



