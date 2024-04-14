# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: ["V": "S001", "V": "S002", "VI": "S001", "VI": "S005", "VII": " S005 ",
# " V ":" S009 ", " VIII":" S007 "]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


# list_dicts = [{"V": "S001", "VI": "S004"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {" VIII": "S007"}]
#
# unique = set()
# for cur_dict in list_dicts:
#     for value in cur_dict.values():
#         unique.add(value)
#
# print(unique)


# Другой способ
# Но работает толко с одним элементом в словаре, т.к. add может добавить только 1 элемент
# unique = set()
# for cur_dict in list_dicts:
#     unique.add(*cur_dict.values())
#
# print(unique)

# Другой способ
# а вот update, расспаковывает все элементы списка, и добавляет каждый элемент во множество
# add добавляет все элементы сразу, к примеру Hello world, а update - по символьно
# аналогично и с кортежами add весь кортеж, а update каждый элемент отдельно
# поэтому update не сможет добавить цифру 55, т.к. не сможет разбить, цифры добавляются через add
# unique = set()
# for cur_dict in list_dicts:
#     unique.update(cur_dict.values())
#
# print(unique)




# dic = {"V": "S001", "V": "S002", "VI": "S001", "VI": "S005", "VII": "S005", " V ": " S009 ", " VIII": " S007 "}
#
# list_1 = list()
# # for i in dic:
# #     list_1.append(dic[i])
# # ИЛИ
# for i in dic.values():
#     list_1.append(i)
#
# # print(list_1)
# print(set(list_1))
# #ИЛИ
# list_1=set(list_1)
# print(list_1)


#
# # А так еще оптимальнее
# mnogh = set()
# for i in dic:
#     mnogh.add(dic[i])
#
# print(mnogh)
#
# # Или
# mnogh2 = set()
# for i in dic.values():
#     mnogh2.add(i)
#
# print(sorted(mnogh2))
