# ✔ Функция получает на вход строку из двух чисел через пробел(дапозон).
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def dict_uni(nums):
# 1 вариант
    # nums = list(map(int, nums.split()))
    # return {chr(num): num for num in range(min(nums), max(nums) + 1)}

# 2 Вариант
#     numbers = nums.split()
#     num1 = int(numbers[0])
#     num2 = int(numbers[1])
#
#     if num1 > num2:
#        num1, num2 = num2, num1
#
#     my_dict = {}
#     for i in range(num1, num2+1):
#         my_dict[chr(i)] = i
#     return my_dict

# 3 Вариант
    nums = list(map(int, nums.split()))
    my_dict = {}
    for i in range(min(nums), max(nums) + 1):
        my_dict[chr(i)] = i
    return my_dict

# text = '30 26'
# print(dict_uni(text))
print(dict_uni('30 26'))



