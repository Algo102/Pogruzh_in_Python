import json
my_dict = {
    "id": 123,
    "name": "Clementine Bauche",
    "username": "Cleba",
    "email": "cleba@corp.mail.ru",
    "address": {
        "street": "Central",
        "city": "Metropolis",
        "zipcode": "123456"
    },
    "phone": "+7-999-123-45-67"
}
res = json.dumps(my_dict, indent=2, separators=(',', ':'), sort_keys=True)
print(res)

# ➢ indent отступы
# ➢ separators Первый — символ разделитель элементов.
#             Второй — разделитель ключа и значения.
# ➢ sort_keys отвечает за сортировку ключей по алфавиту.