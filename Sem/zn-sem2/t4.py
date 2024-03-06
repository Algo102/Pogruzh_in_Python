# Иван Васильевич пришел на рынок и решил купить два арбуза: один для
# себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много
# и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
# Помогите ему! Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

from random import randint

watermelon = int(input("Введите количество арбузов "))
weight = randint(1, 8)
print(weight, end=' ')
max_weight = min_weight = weight

# max_weight = 0
# min_weight = 99

# max_weight = 0
# min_weight = float('inf')

for _ in range(watermelon - 1):
    weight = randint(1, 8)
    print(weight, end=' ')

    # if weight > max_weight:
    #     max_weight = weight
    # if weight < min_weight:
    #     min_weight = weight

    # Вместо ИФ функция мин мах
    min_weight = min(weight, min_weight)
    max_weight = max(weight, max_weight)

print()
print(f'{min_weight = } кг, {max_weight = } кг')