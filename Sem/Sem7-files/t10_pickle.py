import pickle
# передает данные в байтах, соответственно может передавать кастомные классы

class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'My name is {self.name}'

stone = Human('Stone')
# print(stone)

# # Записываем в файл
# with open('example.pickle', 'wb') as file:
#     pickle.dump(stone, file)


# # Читаем из файла, но при чтении класс тоже должен быть активен
with open('example.pickle', 'rb') as file:
    data = pickle.load(file)

print(data)